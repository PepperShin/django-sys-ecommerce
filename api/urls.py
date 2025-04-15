from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

# dev_29
# 바꾼 views 파일들 한번에 끌어오기
from .views import base_views, product_views

# dev_28
app_name = "api"

urlpatterns = [
    path("hello-world/", base_views.hello_world),
    path("hello-world-json/", base_views.hello_world_json),
    path("hello-world-drf/", base_views.hello_world_drf),
    # dev_29
    path("products/", product_views.products_api),
]
