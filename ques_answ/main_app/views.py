from datetime import datetime
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

data_menu = [
    {'page_title': 'Главная', 'page_route': 'home'},
    {'page_title': 'О сайте', 'page_route': 'about'},
]


def index(request) -> HttpResponse:
    data = {
        'title': 'Главная страница',
        'menu': data_menu,
        'page_content': 'Главная'
    }
    return render(request, 'main_app/index.html', context=data)


def question(request, quest_id) -> HttpResponse:
    return HttpResponse(f'Question: {quest_id}')


def archive(request, year):
    if year > 2025:
        uri = reverse('archive', args=(datetime.now().year, ))
        return redirect(uri)
    return HttpResponse(f'Questions arhcive by year: {year}')


def about(request) -> HttpResponse:
    data = {
        'title': 'О сайте',
        'menu': data_menu,
        'page_content':
        'О сайте',
    }
    return render(request, 'main_app/about.html', context=data)


def page_not_found(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound(
        '<h1><b>Страница не найдена!</b></h1>'
        '<a href = "http://127.0.0.1:8000/">'
        'Назад')
