from django.shortcuts import render
import requests
import json

def home(request):

    return render(request, "pages/home.html")

def api():
    #    while True:
            with open('example.txt', 'w', encoding='utf-8') as my_file:
                r = requests.get("https://furn-master.herokuapp.com/api/carousel")
                res = r.json()
                my_dict = res
                my_file.write(json.dumps(my_dict))

        # file = open('templates/pages/home.html', 'w')
        # file.write(res)
        
api()