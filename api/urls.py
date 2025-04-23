from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

# dev_29
# 바꾼 views 파일들 한번에 끌어오기
from .views import base_views, product_views, category_views

# dev_38
from rest_framework import routers

# dev_28
app_name = "api"

# dev_38
router = routers.DefaultRouter()
router.register("categories", category_views.CategoryViewSet)

category_list = category_views.CategoryViewSet.as_view(
    {"get": "list", "post": "create"}
)

category_detail = category_views.CategoryViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)

urlpatterns = [
    # path("hello-world/", base_views.hello_world),
    # path("hello-world-json/", base_views.hello_world_json),
    # path("hello-world-drf/", base_views.hello_world_drf),
    # dev_29
    # http://127.0.0.1:8000/api/products/
    # 방식       url             기능
    # GET       products/       list
    # POST      products/       create
    # GET       products/{id}   product
    # Delete    products/{id}   delete product
    # PUT       products/{id}   modify
    path("products/", product_views.products_api),
    path("product/<int:pk>/", product_views.product_api),
    # dev_32
    # path("categories/", category_views.categories_api),
    # dev_35
    # path("categories/", category_views.CategoriesAPI.as_view()),
    # path("category/<int:pk>/", category_views.CategoryAPI.as_view()),
    # dev_36
    # path("categories/", category_views.CategoriesMixins.as_view()),
    # path("category/<int:pk>/", category_views.CategoryMixins.as_view()),
    # dev_37
    # path("categories/", category_views.CategoriesGeneric.as_view()),
    # path("category/<int:pk>/", category_views.CategoryGeneric.as_view()),
    # dev_38
    # 이렇게 하면 다음 경로들이 자동으로 만들어집니다:
    # GET /categories/
    # POST /categories/
    # GET /categories/<pk>/
    # PUT /categories/<pk>/
    # PATCH /categories/<pk>/
    # DELETE /categories/<pk>/
    path("", include(router.urls)),
    # path("categories/", category_list),
    # path("category/<int:pk>/", category_detail),
]
