from django.shortcuts import render, get_object_or_404
from .cart import Cart  # cart.cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.


# dev_15
def add_cart(request):
    cart = Cart(request)

    print("카트======", cart)

    if request.POST.get("action") == "post":

        # 상품 받아오기
        product_id = int(request.POST.get("product_id"))
        print("product_id", product_id)

        # 상품 개수
        product_qty = int(request.POST.get("product_qty"))
        print("product_qty", product_qty)

        # DB에서 찾아서 product 객체로 변환
        product = get_object_or_404(Product, id=product_id)

        # 세션에 저장
        cart.add(product, product_qty)

        # dev_16
        # 카트 전체 개수 가져오기
        cart_qty = cart.__len__()
        response = JsonResponse({"qty": cart_qty})

        # 세션 확인 테스트
        cart.decrypt_all_sessions()

        # Get Cart Quantity
        return response


# dev_18
def summary_cart(request):
    # 카트 객체 받아오기
    cart = Cart(request)

    return render(request, "cart/summary.html", {"cart": cart})
