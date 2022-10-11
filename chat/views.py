from django.shortcuts import render
import requests


def home(request):
    r = requests.get("https://furn-master.herokuapp.com/api/carousel/1")
    res = r.json()
    context ={
        "api":res
    }
    return render(request, "pages/home.html", context)

