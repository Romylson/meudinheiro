from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def principal(request):
    return HttpResponse('<h1>Olá Mundo Novo - Django</h1>')