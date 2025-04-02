from django.shortcuts import render
from django.http import HttpResponse

from store.models import Product, Category

# Create your views here.


# dev_1
def home(request):
    # dev_5
    products = Product.objects.all()
    return render(request, "store/home.html", {"products": products})


# dev_8
def about(request):
    return render(request, "store/about.html")


# dev_13
def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "store/product.html", {"product": product})


# dev_14
def category_summary(request):
    categories = Category.objects.all()
    return render(request, "store/category_summary.html", {"categories": categories})
