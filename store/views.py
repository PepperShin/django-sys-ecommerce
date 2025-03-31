from django.shortcuts import render
from django.http import HttpResponse

from store.models import Product

# Create your views here.


# dev_1
def home(request):
    # dev_5
    products = Product.objects.all()
    return render(request, "store/home.html", {"products": products})


# dev_8
def about(request):
    return render(request, "store/about.html")
