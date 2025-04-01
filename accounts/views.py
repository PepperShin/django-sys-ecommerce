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

    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            form = RegisterUserForm(request.POST)  # 모델에 값을 입력
            if form.is_valid():
                form.save()  # 회원 DB 저장

                # 회원 가입 후 자동 로그인
                username = form.cleaned_data.get("username")
                raw_password = form.cleaned_data.get("password1")

                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect("/")
    else:
        form = RegisterUserForm()

    return render(request, "accounts/register.html", {"form": form})
