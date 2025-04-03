from django.contrib import admin
from django.urls import path, include
from . import views

# dev_8
app_name = "store"

# dev_1
urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),  # dev_8 어바웃 페이지 추가
    path(
        "product/<int:product_id>", views.product, name="product"
    ),  # dev_13 제품 상세 페이지
    path(
        "category_summary", views.category_summary, name="category_summary"
    ),  # dev_14 카테고리
    path(
        "category/<int:category_id>", views.category, name="category"
    ),  # dev_14 카테고리 처리
]
