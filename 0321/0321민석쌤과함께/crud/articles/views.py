from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {"articles" : articles}
    return render(request, "articles/index.html", context)

def create(request):    
    if request.method == "POST": # post는 데이터에 저장하는 것
        # 입력을 받아서 처리하는 과정
        # 모델에서 사용했던 name을 그대로 사용한다.
        # POST 요청을 처리한다
        # title = request.POST.get("title")
        # content = request.POST.get("content")
        # article = Article(title=title, content=content)
        # article.save()
        # 저장하고 어디로 갈지 정해준다

        form = ArticleForm(request.POST, request.FILES) # 이미지 파일은 따로 처리해야함. 따라서 request.FILES를 넣어줘야함
        if form.is_valid():
            article = form.save()
            # 만약 상세페이지를 갈 때 pk값을 필요로 하기 때문에
            return redirect("articles:detail", article.pk)
        
    else:
        form = ArticleForm()

    context = {"form" : form}
    return render(request, "articles/create.html", context)

def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {"article" : article}
    return render(request, "articles/detail.html", context)

def update(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        form =ArticleForm(request.POST, request.FILES, instance=article)    # 파일 수정하기 위해서 request.FILES 인자로 넘기기
        if form.is_valid():
            form.save()
            return redirect("articles:detail", article.pk) # 누구를 수정할지 알아야해서 pk값이 필요함
    else:
        form = ArticleForm(instance=article)    # 현재 article 폼 활용
    context = {"form" : form,
               "article": article}
    return render(request, "articles/update.html", context)



def delete(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return redirect("articles:index")   # 누구를 지울지 pk가 없어도 되기 때문에 article.pk를 명시할 필요가 없음