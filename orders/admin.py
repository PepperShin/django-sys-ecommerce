from django.contrib import admin
from orders.models import Order, OrderItem

# dev_24
admin.site.register(Order)
admin.site.register(OrderItem)
