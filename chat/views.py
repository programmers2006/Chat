from django.shortcuts import render
import requests


def home(request):

    return render(request, "pages/home.html")

def api():
    while True:
        r = requests.get("https://furn-master.herokuapp.com/api/carousel/")
        res = r.json()
        file = open('sup.css', 'w')
        file.write(str(res))

api()