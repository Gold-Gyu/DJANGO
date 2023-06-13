from django.shortcuts import render

# Create your views here.
def calculation(request):

    return render(request, "calculators/calculation.html")

def result(request):
    num1 = int(request.GET.get("num1"))
    num2 = int(request.GET.get("num2"))
    if num2 == 0:
        result = "계산할 수 없습니다."
    else:
        result = num1 / num2
    result2 = num1 * num2
    result3 = num1 - num2
    context = {
        "num1" : num1,
        "num2" : num2,
        "result" : result,
        "result2" : result2,
        "result3" : result3
    }
    return render(request, "calculators/result.html", context)