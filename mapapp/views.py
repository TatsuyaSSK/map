from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.

def mainfunc(request): 
    if request.method == "POST":
        #requestと共に、station,ramen,walktime が取得できる 
        station = {
            "station":request.POST["station"],
            "ramen":request.POST["ramen"],
            "walktime":request.POST["walktime"],
        }
        return render(request,"map.html",station)
    return render(request,"main.html",{})

def mapfunc(request,station):
    if request.method == "POST":
        return redirect("main")
    return render(request,"map.html",{"station":station})
