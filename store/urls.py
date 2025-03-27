from django.contrib import admin
from django.urls import path, include
from . import views

# dev_1
urlpatterns = [
    path("", views.home, name="home"),
]
