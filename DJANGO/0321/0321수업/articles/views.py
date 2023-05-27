from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


# def new(request):
#     return render(request, 'articles/new.html')


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)    # request.POST
        if form.is_valid():         # 유효하다면
            article = form.save()   # 알아서 연결되어있는 모델을 통해 생성한다.
            return redirect('articles:detail', article.pk)
        return redirect('articles:create')
        
        # 모델폼은 save를 해주게되면 자동으로 안에있는 값을 알맞은 곳에 넣고 반환해줌
        # 즉 article = form.save()한줄이
        """
        article = Article(title=title, content=content)
        content=content()
        article.save()
        """
        # 와 같다
        # 위 코드로 모델을 통해서 데이터를 생성할 수 있다.

    else:   # GET일 때
        form = ArticleForm()

    context = {"form": form}
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {'article': article}
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 이전의 article가져옴
    if request.method == "POST":
        # 비어있는 폼이 아니라 유저로부터 받은 데이터로 채움
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk=article.pk)
    
    else:   # GET일 때
        form = ArticleForm(instance=article)    # 비어있는 폼이 아니라 기존 article을 채운 폼이어야한다. 이럴 때 instance를 쓴다.

    context = {'form': form}
    return render(request, 'articles/update.html', context)
