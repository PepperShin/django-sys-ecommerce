from django.shortcuts import render, redirect
from django.contrib import messages
from cart.cart import Cart
from store.models import Product
from .models import Order, OrderItem

# dev_25
from django.contrib.auth.decorators import login_required


# dev_25
@login_required(login_url="accounts:login_user")
# dev_24
def create_orders(request):
    if request.POST:
        cart = Cart(request)

        if request.user.is_authenticated:
            user = request.user

            # Order(주문) 생성 및 저장
            create_order = Order(user=user)
            create_order.amount_paid = cart.get_product_total()  # 주문 총액
            create_order.save()

            # Order Items 생성 및 저장
            order_id = create_order.pk
            for item in cart:
                print(item)

                create_order_item = OrderItem(
                    order_id=order_id,  # 컬럼명 방식 또는 객체 방식인 order = create_order
                    product_id=item["product"].id,
                    quantity=item["quantity"],
                    price=item["price"],
                )
                create_order_item.save()

            # 만약 카트도 지우고 싶다면
            cart_keys = list(cart.get_cart().keys())
            for product_id in cart_keys:
                product = Product.objects.get(id=product_id)
                cart.remove(product)

            messages.success(request, "주문이 완료되었습니다.")
            return redirect("/")

        else:
            messages.success(request, "주문을 위해선 로그인을 하셔야 합니다.")
            return redirect("/")
    else:
        # dev_25
        # messages.success(request, "잘못된 접근입니다.")
        return render(request, "orders/create.html")
