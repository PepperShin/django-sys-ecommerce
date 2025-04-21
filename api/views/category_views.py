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

# dev_37
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError, PermissionDenied


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


# dev_37
# from rest_framework.generics import ListCreateAPIView
# generics.CreateAPIView : 생성
# generics.ListAPIView : 목록
# generics.RetrieveAPIView : 조회
# generics.DestroyAPIView : 삭제
# generics.UpdateAPIView : 수정
# generics.RetrieveUpdateAPIView : 조회/수정
# generics.RetrieveDestroyAPIView : 조회/삭제
# generics.ListCreateAPIView : 목록/생성
# generics.RetrieveUpdateDestroyAPIView : 조회/수정/삭제

# 권한
# AllowAny: 누구나 접근 가능
# IsAuthenticated: 로그인 한 사용자만 접근 가능
# IsAdminUser: is_staff=True인 관리자만 접근 가능
# IsAuthenticatedOrReadOnlyL: 읽기는 모두 허용, 쓰기는 인증 사용자만 가능


class CategoriesGeneric(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):  # mixins의 create를 오버라이딩
        name = request.data.get("name")
        # 같은 이름의 카테고리가 이미 존재할 경우 오류 메세지
        if Category.objects.filter(name=name).exists():
            raise ValidationError({"message": "같은 이름의 카테고리가 있습니다."})

        response = super().create(
            request, *args, **kwargs
        )  # 실제 create 액션은 여기서 실행
        response.data = {
            "message": "카테고리가 성공적으로 생성 되었습니다.",
            "category": response.data,
        }

        return response


# 단일 인스턴스
class CategoryGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySimpleSerializer

    # 조회 시 로그 찍기
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        print(f"조회 카테고리 ID {instance.id} - {instance.name}")

        return super().retrieve(request, *args, **kwargs)

    # 수정 시 로깅 및 응답 커스터마이징
    def update(self, request, *args, **kwargs):

        instance = self.get_object()
        print(f"수정 카테고리 이름 {instance.name} - {request.data.get('name')}")
        response = super().update(request, *args, **kwargs)
        response.data = {
            "message": f"수정 카테고리 이름 {instance.name} - {request.data.get('name')}",
            "category": response.data,
        }

        return response

    # HTTP DELETE 요청 ->
    # destroy() 실행 ->
    # perform_destroy(instance) 호출 ->
    # 객체 삭제

    def perform_destroy(self, instance):
        if instance.name == "자바":
            raise PermissionDenied("이 카테고리는 관리자만이 삭제 가능합니다.")

        print(f"[삭제] 카테고리 {instance.name} 삭제됨")
        instance.delete()

    # 삭제 응답 커스터마이징
    def destroy(self, request, *args, **kwargs):
        self.perform_destroy(self.get_object())

        return Response(
            {"message": "카테고리가 삭제되었습니다."},
            status=status.HTTP_204_NO_CONTENT,
        )
