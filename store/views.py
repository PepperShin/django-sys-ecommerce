from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# dev_1
def home(request):
    return render(request, "store/home.html", {})
    # return HttpResponse("<h1>이제부터 쇼핑몰을 만들어 봅시다.</h1>")
