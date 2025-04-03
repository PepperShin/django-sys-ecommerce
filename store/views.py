from django.shortcuts import render, redirect
from django.http import HttpResponse

from store.models import Product, Category
from django.contrib import messages

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


# dev_14
def category(request, category_id):

    try:
        category = Category.objects.get(id=category_id)
        # category = Category.objects.filter(id=category_id) #query_set

        # select * from product , category where product.category_id =  category.id
        # category = models.ForeignKey(Category, on_delete=models.CASCADE)
        products = Product.objects.filter(category=category)

        context = {
            "category": category,
            "products": products,
        }
        return render(request, "store/category.html", context)

    except:
        messages.success(request, ("카테고리가 존재 하지 않습니다."))
        return redirect("store:home")
