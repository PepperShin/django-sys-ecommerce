from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from store.models import Product
from api.serializers.product_serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status


# dev_29
@api_view(["GET", "POST"])
def products_api(request):
    if request.method == "GET":
        products = Product.objects.all()
        # many=True ➜ 여러 개의 인스턴스 (QuerySet, 리스트 등)
        # many=False (기본값) ➜ 단일 인스턴스
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # dev_30
    # 디시리얼라이져
    if request.method == "POST":
        print("데이터", request.data)  # json, dic
        print("타입", type(request.data))  # dic

        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


# dev_30
@api_view(["GET", "DELETE", "PUT"])
def product_api(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == "GET":
        # many=True ➜ 여러 개의 인스턴스 (QuerySet, 리스트 등)
        # many=False (기본값) ➜ 단일 인스턴스(이번에는 세팅할 필요 없다)
        serializer = ProductSerializer(product)  # 딕셔너리로 전환

        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        product.delete()

        return Response(
            "SUCCESS", status=status.HTTP_204_NO_CONTENT
        )  # from rest_framework import status
