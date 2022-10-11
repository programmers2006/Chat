from django.shortcuts import render
import requests
import json

def home(request):

    return render(request, "pages/home.html")

def api():
<<<<<<< HEAD
    #    while True:
            with open('example.txt', 'w', encoding='utf-8') as my_file:
                r = requests.get("https://furn-master.herokuapp.com/api/carousel")
                res = r.json()
                my_dict = res
                my_file.write(json.dumps(my_dict))

        # file = open('templates/pages/home.html', 'w')
        # file.write(res)
=======
    while True:
        r = requests.get("https://furn-master.herokuapp.com/api/carousel/")
        res = r.json()
        file = open('templates/pages/home.html', 'w')
        file.write(str(res))
>>>>>>> fb631bcf5338a4f5c424fd0c149fdb3cb1d6ce1e

api()