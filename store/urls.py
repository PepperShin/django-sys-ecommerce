from django.contrib import admin
from django.urls import path, include
from . import views

# dev_8
app_name = "store"

# dev_1
urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),  # dev_8 어바웃 페이지 추가
]
