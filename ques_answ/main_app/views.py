from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):  # HttpRequest
    return HttpResponse('Ответы на вопросы')
