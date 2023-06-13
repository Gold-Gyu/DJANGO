from django.shortcuts import render, redirect
# 로그인 정보를 입력할 때 필요한 폼가져오기
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Create your views here.
def login(request):

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("articles:index")
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    form = AuthenticationForm()
    context = {"form" : form}
    auth_logout(request)
    # return redirect("articles:index")
    return render(request, "accounts/babo.html", context)

def signup(request):

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:index")

    else:
        form = CustomUserCreationForm()
    context = {
        "form":form
    }
    return render(request, "accounts/signup.html", context)



def delete(request):
    request.user.delete()
    auth_logout(request)    # 로그아웃해주기
    return redirect("articles:index")


def update(request):
    if request.method =="POST":
        form = CustomUserChangeForm(data=request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect("articles:index")

    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form":form}
    return render(request, "accounts/update.html", context)


def change_password(request):
    if request.method == "POST":
        # 변경시 로그인 유지
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form" : form
    }
    
    return render(request, "accounts/password.html", context)
