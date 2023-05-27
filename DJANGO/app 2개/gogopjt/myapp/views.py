from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "myapp/index.html")

def profile(request):
    name = "KeumGyu"
    age = 25

    info = {"name": name, "age": age}
    return render(request, "myapp/profile.html", info)

def fruits(request):
    f_list = ["apple" , "banana" , "melon"]
    context = {
        "fruits" : f_list
    }
    return render(request, "myapp/fruits.html", context)
    
def template(request):
    return render(request, "myapp/template.html")
