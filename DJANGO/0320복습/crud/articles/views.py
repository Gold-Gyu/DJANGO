from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {"articles":articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {"article" : article}
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, "articles/new.html")

def create(request): 
    # 데이터베이스 저장
    # 1. 사용자 입력 정보를 가져온다
    # 2. 데이터 정보를 저장한다.
    # 사용자정보는 request에 있다
    title = request.POST.get('title')
    content = request.POST.get("content")
    article = Article(title=title, content=content)
    article.save()
    return redirect("articles:index")

def delete(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        "article":article
    }
    return render(request, "articles/edit.html", context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get("title")
    article.content = request.POST.get("content")
    article.save()
    return redirect("articles:detail", article.pk)
