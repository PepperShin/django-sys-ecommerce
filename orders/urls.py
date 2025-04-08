from django.urls import path
from orders import views

# dev_24
app_name = "orders"

urlpatterns = [
    path("create/", views.create_orders, name="create_orders"),
]
