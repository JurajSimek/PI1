from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Ahoooooj ja som Jurko Šimek. Vitaj u nás!</h1>')