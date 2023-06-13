from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(id=pk)
    # article함수를 하나가 가져온다.
    context = {"article": article}
    # context에 담아서 랜더로 전송
    return render(request, 'articles/detail.html', context)
    # articles파일 아래 detail.html에 context를 담아서 전송

def new(request):

    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    article = Article(title=title, content=content)
    article.save()
    
    return redirect('articles:detail', article.pk)
    # forward방식: 요청과 응답 정보를 그대로 계속 가져감, 페이지만 바뀐다. url은 그대로 유지된 상태에서 안의 페이지만 바꾼다. url은 초기 상태를 유지하면서 페이지만 바꿈 => 보통 시스템의 변화가 생기지 않는 단순 조회 요청을할 때 forward 방식을 사용한다.
    # redirect 방식 : 아예 새로운 요청을 생성(기존의 요청, 응답 정보가 제거됨을 의미) + url도 변경이됨 => 시스템에 변화가 생기는 새로운 요청
    # redirect : 어디에다가 다시 요청을 보낼까를 의미함 
    # render : 현재 페이지를 유지한상태에서 다음 페이지를 어디로 보여줄지 :

# 삭제기능
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect("articles:index")

# 수정기능
# 오로지 보여주는 것
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article" : article
    }
    return render(request, "articles/edit.html", context)

# 데이터를 바꾸는 곳
def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get("title")
    article.content = request.POST.get("content")
    article.save()
    return redirect("articles:detail", article.pk)