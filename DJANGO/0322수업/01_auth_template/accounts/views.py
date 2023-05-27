from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.
def login(request):
    if request.method == 'POST':    # 데이터 베이스를 조작하는 요청(로그인)
        # 로그인 처리를 해줌
        # 유저가 입력한 정보가져오기
        form = AuthenticationForm(request, request.POST)
        # request인자가 하나 더 들어가는 이유
        # 요청 들어온 애한테 쿠키담아서 넘겨줘야하기 때문에

        if form.is_valid():
            # 있으면 user를 나한테 돌려줘라
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:   # 맨 처음 로그인 화면을 달라는 것과 같음
        # 비어있는 로그인 페이지를 제공
        form = AuthenticationForm()
    
    context = {'form':form}
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')