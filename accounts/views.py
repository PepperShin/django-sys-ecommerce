from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# from .forms import RegisterUserForm 상대경로
from accounts.forms import RegisterUserForm  # 절대경로

# Create your views here.


# dev_9
def login_user(request):

    if request.method == "POST":
        # username = request.POST.get("username", "") 이게 더 안전한 표현
        username = request.POST["username"]
        password = request.POST["password"]
        """
        POST 는 request 객체 안에 저장되어있는 딕셔너리 타입.
        class HTTPRequest:
            POST = {"username" : "admin", "password" : "1234"}
        """
        # DB에 있는지를 조회 후 대조
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You Have been logged in")
            return redirect("/")
        else:
            messages.success(request, ("There was an error, please try again"))
            return redirect("accounts:login_user")  # /accounts/login
    else:
        return render(request, "accounts/login.html", {})


def logout_user(request):
    logout(request)  # session에 저장된 sessionid 삭제
    return redirect("/")


# dev_10
def register_user(request):
    form = RegisterUserForm()

    if request.method == "POST":
        print(form)
    else:
        context = {"form": form}

    return render(request, "accounts/register.html", context)
