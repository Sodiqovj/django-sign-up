from django.shortcuts import render, redirect
from .form import Login
from mysite.models import *

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect("/")
    else:
        form = Login()
        
    return render(request, "form.html", {"form": form})
