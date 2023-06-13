from django.shortcuts import render,redirect
from .models import Movie
from .forms import MoviesForm
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        "movies" : movies
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == "POST":    # create.html에서 submit을 눌러서 POST로 데이터가 들어오면
        form = MoviesForm(request.POST, request.FILES) # POST로 들어온 값과 FILES로 들어온 값을 form에 담아서
        if form.is_valid(): # 유효성을 검사하고
            movie = form.save() # movie에 저장한다.
            return redirect("movies:detail", movie.pk)  # 위의 movie로 정의한 값에서 pk값을 넣어 urls.py의 detail로 보낸다.
    else:   # index.html의 a테그 안에서 create로 이동할 때 get데이터 전송
        form = MoviesForm()
    context = {"form":form}
    return render(request, "movies/create.html", context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {"movie" : movie}
    return render(request, 'movies/detail.html', context)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":   # update.html에서 보냔 POST 데이터가 들어오면
        form = MoviesForm(request.POST, request.FILES, instance=movie)    # POST값, 이미지파일, 기존 request에서 수정 순서대로 인자 생성
        if form.is_valid(): # 유효성 체크
            form.save() # 저장
            return redirect("movies:detail", movie.pk)
    else:
        form = MoviesForm(instance=movie)   # 수정할 떄는 기존 데이터를 가지고 form에 넣어서 수정한다
    context = {"form":form,
               "movie":movie} # movie의 pk값을 보내줘야하기 때문에 movie값도 context에 넣어준다
    return render(request, "movies/update.html", context)

def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect("movies:index")   # 누구를 지울지 pk가 없어도 되기 때문에 article.pk를 명시할 필요가 없음