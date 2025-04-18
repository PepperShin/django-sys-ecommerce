from django.test import TestCase
import pickle

# Create your tests here.


# dev_28 시리얼라이제이션의 이해
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


class ObjectAPITest(TestCase):
    def setUp(self):
        pass

    def test_path(self):
        dict = {
            "add": add,
            "sub": sub,
        }
        url = "add"
        print(dict[url](1, 2))
        print(dict["sub"](2, 1))

    # 사각형 rect 객체를 직렬화 (Serialization)
    def test_serialization(self):
        rect = Rectangle(10, 20)

        with open(
            "rect.data", "wb"
        ) as f:  # open은 rect.data 를 열어서 wb(write binary)로 저장한다.
            pickle.dump(
                rect, f
            )  # pickel이 직렬화 함수. rect 클래스 객체를 f에 직렬화 하여 저장(바이너리)

        # 역직렬화 (Deserialization)
        with open("rect.data", "rb") as f:
            r = pickle.load(f)

        print(r.width, r.height)


from rest_framework.views import APIView
from store.models import Category
from api.serializers.category_serializers import (
    CategorySerializer,
    CategorySimpleSerializer,
)
from rest_framework import status
from rest_framework.response import Response


class CategoriesAPI(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    simple_serializer_class = CategorySimpleSerializer

    def get_queryset(self):
        return self.queryset

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def get_simple_serializer(self, *args, **kwargs):
        return self.simple_serializer_class(*args, **kwargs)

    def get(self, request):
        categories = self.get_queryset()
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_simple_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # 예: id를 request에서 받았다고 가정
        category_id = request.data.get("id")
        try:
            category = self.get_queryset().get(id=category_id)
        except Category.DoesNotExist:
            return Response(
                {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_simple_serializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        category_id = request.data.get("id")
        try:
            category = self.get_queryset().get(id=category_id)
            category.delete()
            return Response(
                {"message": "Category deleted"}, status=status.HTTP_204_NO_CONTENT
            )
        except Category.DoesNotExist:
            return Response(
                {"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND
            )
