from django.urls import path
from . import views

# dev_24
app_name = "payment"

urlpatterns = [
    path("process/", views.payment_process, name="payment_process"),
]
