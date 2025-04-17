from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

# dev_29
# 바꾼 views 파일들 한번에 끌어오기
from .views import base_views, product_views, category_views

# dev_28
app_name = "api"

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
    path("categories/", category_views.CategoriesAPI.as_view()),
]
