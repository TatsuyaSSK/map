from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
import json

# Create your views here.

def mainfunc(request): 
    if request.method == "POST":
        #駅、チェックボックスのあるなしで、どのjsonファイルを開くか限定する
        station = request.POST["station"]
        lesson = request.POST.getlist("lesson")
        json_files = []
        for les in lesson:
            json_open = open("static/{station}/{les}.json".format(station = station,les = les),"r")
            json_load = json.load(json_open)
            json_files.append(json_load)
            #requestと共に、station,ramen,walktime が取得できる 
        dic = dict(list(enumerate(json_files)))
        dic = {
            "station":request.POST["station"],
            "walktime":request.POST["walktime"],
            #受け渡すjsonファイルをチェックの有無によって決定
            "tabelog":json.dumps(json_files[0][0:30],ensure_ascii=False),
            "tabelog2":json.dumps(json_files[1][30:60],ensure_ascii=False),
        }
        return render(request,"map.html",dic)
        
    return render(request,"main.html",{})

def mapfunc(request):
    if request.method == "POST":
        return redirect("main")
    return render(request,"map.html",{"station":station})
