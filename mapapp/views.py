from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
import json
import geocoder

# Create your views here.

def mainfunc(request): 
    if request.method == "POST":
        print(request.POST)
        #住所を座標に変換
        address = request.POST["address"]
        location_list = geocoder.osm(address, timeout=5.0).latlng
        location = (location_list[0],location_list[1])
        #stationには座標が格納されている
        lessons = request.POST.getlist("lessons")
        json_files = []
        #swimming.jsonの中から、距離が20分以内のものだけ表示、みたいなことをする
        for lesson in lessons:
            json_open = open("static/{lesson}.json".format(lesson = lesson),"r")
            json_load = json.load(json_open)
            #json形式に変換
            json_dumps = json.dumps(json_load,ensure_ascii=False)
            json_files.append(json_dumps)
            
        #辞書型配列を作成
        dic = dict(jsons=json_files,lessons = request.POST.getlist("lessons"),location = location,address = address)
        #map.htmlに渡す
        return render(request,"map.html",dic)
        
    return render(request,"main.html",{})

def mapfunc(request):
    if request.method == "POST":
        return redirect("main")
    return render(request,"map.html")
