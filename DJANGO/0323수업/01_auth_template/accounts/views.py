from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
## 빌트인 폼 가져오기
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())    # 로그인처리
            return redirect('articles:index')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)    # 세션정보지우기
    return redirect('articles:index')

def signup(request):    # 회원가입
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    
    else:   # 
        form = CustomUserCreationForm()
    context = {
        "form": form
    }
    return render(request, 'accounts/signup.html', context)

def delete(request):
    
    # 어떤 유저인지 가져오고
    # 나한테 요청한 request를 가지고 있어야함(로그인해있는 유저)
    # 즉, request의 유저를 가져온다
    user = request.user
    # 지우고
    user.delete()
    # 위치 개중요 ★ user를 지우고 나서 세션정보도 지운다.
    auth_logout(request)
    return redirect('articles:index')

def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST,instance=request.user)   #request.POST => 유저가 입력한 정보를 가져온것, instance=user
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form" : form
    }
    return render(request, 'accounts/update.html', context)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)    #★★★비밀번호변경시 로그인 유지
            return redirect('articles:index')

    else:
        form =PasswordChangeForm(request.user)
    context={"form":form}
    return render(request, 'accounts/change_password.html', context)