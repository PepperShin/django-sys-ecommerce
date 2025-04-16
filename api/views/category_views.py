from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from store.models import Product, Category
from api.serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import status


# dev_32
@api_view(["GET"])
def categories_api(request):
    if request.method == "GET":
        products = Category.objects.all()
        # many=True ➜ 여러 개의 인스턴스 (QuerySet, 리스트 등)
        # many=False (기본값) ➜ 단일 인스턴스
        serializer = CategorySerializer(products, many=True)
        return Response(serializer.data)
