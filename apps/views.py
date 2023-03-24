from django.http import HttpResponse
from django.shortcuts import render
import wikipedia


def home(request):
    if request.method == "POST":
        search = request.POST["search"]
        try:
            result = wikipedia.summary(search, sentences=50)
        except:
            return HttpResponse('Wrong input')
        return render(request, "main/index.html", {"result" : result})
    return render(request, "main/index.html")