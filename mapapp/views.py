from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
import json

# Create your views here.

def mainfunc(request): 
    if request.method == "POST":
        #駅、チェックボックスのあるなしで、どのjsonファイルを開くか限定する
        station = request.POST["station"]
        lessons = request.POST.getlist("lessons")
        json_files = []
        for lesson in lessons:
            json_open = open("static/{station}/{lesson}.json".format(station = station,lesson = lesson),"r")
            json_load = json.load(json_open)
            json_dumps = json.dumps(json_load[0:30], ensure_ascii=False)
            #試しに10個渡す
            json_files.append(json_dumps)

        #辞書型配列を作成
        dic = dict(zip(lessons,json_files))
        dic["station"] = request.POST["station"]
        dic["walktime"] = request.POST["walktime"]
        dic["lessons"] = request.POST.getlist("lessons")

        #map.htmlに渡す
        return render(request,"map.html",dic)
        
    return render(request,"main.html",{})

def mapfunc(request):
    if request.method == "POST":
        return redirect("main")
    return render(request,"map.html",{"station":station})
