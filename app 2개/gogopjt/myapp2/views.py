from django.shortcuts import render

# Create your views here.
def hello(request, name):   # 받아줘서 다른 이름을 받아도 그 이름이 뜨게 만드는 것
    context = {"name" : name}
    return render(request, "myapp2/hello.html", context)