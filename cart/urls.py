from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cart import views

# dev_15
app_name = "cart"

urlpatterns = [
    path("add/", views.add_cart, name="add_cart"),
]
