from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Create your views here.
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # form.save()
            auth_login(request, form.get_user())    # 로그인 처리
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    context = {"form" : form}
    return render(request, "accounts/login.html", context)

def logout(request):
    auth_logout(request)    # 세션정보지우기
    return redirect("movies:index")

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            auth_login(request, user)
            return redirect("movies:index")
    else:
        form = CustomUserCreationForm()
    context = {"form" : form}
    return render(request, "accounts/signup.html", context)

def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("movies:index")