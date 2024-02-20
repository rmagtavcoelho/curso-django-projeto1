from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Renato Magno Tavares Coelho'
    })


def contato(request):
    return HttpResponse('contato 3')


def sobre(request):
    return HttpResponse('sobre 3')
