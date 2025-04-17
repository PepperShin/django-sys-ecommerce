from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from store.models import Product, Category
from api.serializers import ProductSerializer
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
    # if request.method == "POST":
    #     print("데이터", request.data)  # json, dic
    #     print("타입", type(request.data))  # dic

    #     serializer = ProductSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data)

    # dev_33_2 view에서 직접 처리하기
    if request.method == "POST":

        # request.data는 기본적으로 불변. category부분만 pop이 불가능
        data = request.data.copy()

        # 복사해서 pop 가능
        category_data = data.pop("category")
        # category_data = request.data["category"]

        # get_or_create 는 dict 형식으로 받기 때문에 category_data는 리스트 일 수 있어서 확인
        if isinstance(category_data, list):
            category_data = category_data[0]

        category, _ = Category.objects.get_or_create(**category_data)

        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(category=category)

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
