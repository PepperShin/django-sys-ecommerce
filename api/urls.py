from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from api.views import hello_world, hello_world_json, hello_world_drf

# dev_28
app_name = "api"

urlpatterns = [
    path("hello-world/", hello_world),
    path("hello-world-json/", hello_world_json),
    path("hello-world-drf/", hello_world_drf),
]
