# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("hello world")
    return render(request, "home.html")


def about(request):
    # return HttpResponse("<h1>This is about page</h1>")
    return render(request, "about.html")
