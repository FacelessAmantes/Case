from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello METANIT.COM")


def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")


def authorisation(request):
    
    return HttpResponse()