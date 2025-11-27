from datetime import datetime
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404


from . import models

# Create your views here.

data_menu = [
    {'page_title': 'Главная', 'page_route': 'home'},
    {'page_title': 'О сайте', 'page_route': 'about'},
]


def index(request) -> HttpResponse:
    questions: models.QuestionManager = models.Question.published.all()
    data = {
        'title': 'HELP WTF',
        'menu': data_menu,
        'questions': questions,
    }
    return render(request, 'main_app/index.html', context=data)


def about(request) -> HttpResponse:
    data = {
        'title': 'О сайте',
        'menu': data_menu,
        'page_content': 'О сайте',
    }
    return render(request, 'main_app/about.html', context=data)


def question(request, quest_id):
    quest_by_id = get_object_or_404(models.Question, pk=quest_id)
    data = {
        'title': quest_by_id.title,
        'question_content': quest_by_id.content,
        'create time': quest_by_id.time_create,
        'menu': data_menu,
    }
    return render(request, 'main_app/question.html', data)


def page_not_found(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound(
        '<h1><b>Страница не найдена!</b></h1>'
        '<a href = "http://127.0.0.1:8000/">'
        'Назад')
