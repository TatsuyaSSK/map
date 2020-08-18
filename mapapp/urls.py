from django.urls import path
from .views import mainfunc,mapfunc

urlpatterns = [
    path("main/",mainfunc,name = "main"),
    path("map/",mapfunc,name = "map"),
]
