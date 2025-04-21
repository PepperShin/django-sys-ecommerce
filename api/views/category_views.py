from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from store.models import Category
from api.serializers.category_serializers import (
    CategorySerializer,
    CategorySimpleSerializer,
)
from rest_framework.response import Response

# dev_35
from rest_framework.views import APIView
from rest_framework import status


# dev_32
@api_view(["GET"])
def categories_api(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


# dev_35
class CategoriesAPI(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySimpleSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def put(self, request):
        pass

    def delete(self, request):
        pass


class CategoryAPI(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        serializer = CategorySimpleSerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        serializer = CategorySimpleSerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        category.delete()

        return Response(
            "삭제 성공", status=status.HTTP_204_NO_CONTENT
        )  # from rest_framework import status


from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView


# dev_36
# GenericAPIView: self.get_queryset()과 self.get_serializer()를 제공
# ListModelMixin: self.list() 내부에서 위의 메서드들을 호출
# 주의
# 기본적으로는 queryset, serializer_classs는 약속된 이름
# 대신 커스텀 마이징은 가능
class CategoriesMixins(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# 커스터마이징
"""
class CategoriesCustomMixins(ListModelMixin, CreateModelMixin, GenericAPIView):
    categories = Category.objects.all()
    category_serializer = CategorySimpleSerializer

    # GenericAPIView의 get_queryset 함수를 오버라이드 해서 queryset 대신 categories를 리턴
    def get_queryset(self): 
        return self.categories
    
    # GenericAPIView의 get_serializer_class 함수를 오버라이드 해서 serializer_class 대신 category_serializer를 리턴
    def get_serializer_class(self):
        return self.category_serializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

"""

from rest_framework.mixins import (
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)


class CategoryMixins(
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # lookup_field = "name"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)
