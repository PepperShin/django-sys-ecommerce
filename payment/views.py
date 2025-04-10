from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from orders.models import Order, OrderItem
from .models import Payment
from store.models import Product
from django.contrib import messages
from django.http import HttpResponse

from orders.forms import ShippingForm


# dev_26
@login_required(login_url="accounts:login_user")
def payment_process(request):
    # 결제 성공 시 로직
    # 1. 주문 정보 저장을 위해 ajax 요청
    # 2. 서버에서 결제 금액과 주문금액(세션에 저장되어있는)이 일치 하는지 확인
    # 3. 일치하면 주문 정보 및 결제정보 저장
    if request.POST:
        cart = Cart(request)
        # 실제는 100이 아닌 cart의 get_product_total과 비교
        if 100 == int(request.POST["paid_amount"]):

            # 로그인 유저
            user = request.user

            # 주문정보 생성 및 저장
            create_order = Order(user=user)
            create_order.amount_paid = cart.get_product_total()  # 총액
            create_order.save()

            # 주문 생성 후 주문번호를 바탕으로 주문 아이템 생성
            order_id = create_order.pk

            for item in cart:
                create_order_item = OrderItem(
                    order_id=order_id,
                    product_id=item["product"].id,
                    quantity=item["quantity"],
                    price=item["price"],
                )

                create_order_item.save()

            # dev_26_2
            # 배송지 정보 저장
            form = ShippingForm(request.POST)

            if form.is_valid():
                shipping = form.save(commit=False)
                shipping.user = request.user
                shipping.order = create_order
                shipping.save()

            # 결제 정보 저장
            create_payment = Payment(order=create_order)
            create_payment.imp_uid = request.POST["imp_uid"]
            create_payment.save()

            # Delete cart item(만약 카트도 지우고 싶다면)
            cart_keys = list(cart.get_cart().keys())
            for product_id in cart_keys:
                product = Product.objects.get(id=product_id)
                cart.remove(product)

            messages.success(request, "결제가 완료되었습니다.")
            # dev_26_2
            return redirect("/")

        else:
            messages.success(request, "결제금액이 맞지 않아 취소되었습니다.")
            return redirect("/")
