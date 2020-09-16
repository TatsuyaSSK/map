from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
import json
import geocoder
import geopandas as gpd
from geopy.distance import geodesic

# Create your views here.

def mainfunc(request): 
    if request.method == "POST":
        #習い事を取得
        lessons = request.POST.getlist("lessons")
        #住所を座標に変換
        address = request.POST["address"]
        location_list = geocoder.osm(address, timeout=5.0).latlng
        location = (location_list[0],location_list[1])
        json_files = []
        for lesson in lessons:
            json_open = open("static/{lesson}.json".format(lesson = lesson),"r")
            json_load = json.load(json_open)
            #入力された住所から徒歩20分以内（距離が1.6km）のもののみ抽出
            json_load_selected = []
            for j in range(len(json_load)):
                json_location = (json_load[j]["緯度"],json_load[j]["経度"])
                dis = geodesic(location,json_location).m
                walktime = round(dis / 80)
                json_load[j]["walktime"] = walktime
                if walktime <= 10:
                    json_load_selected.append(json_load[j])
            #json形式に変換
            json_dumps = json.dumps(json_load_selected,ensure_ascii=False)
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
