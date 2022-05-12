from django.shortcuts import render

from .models import *


def home(request):
    return render(request, "home.html")
def blog(request):
    A = Maqola.objects.all()
    return render(request, "blog.html", {"maqola": A})
def about(request):
    return render(request, "about.html")
def maqola(request):
    return render(request, "maqola.html")
def interviyu(request):
    A = Interviyu.objects.all()
    return render(request, "intervyu.html", {"inter": A})
