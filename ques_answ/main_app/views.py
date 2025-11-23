from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

# Create your views here.


def index(request):
    print(f'request.GET: {request.GET}')
    return HttpResponse('<h1>1337Question1337</h1>'
                        '<p><b>Menu</b></p>'
                        '<a href = "http://127.0.0.1:8000/questions/">'
                        'Всe вопросы')


def question(request, quest_id):
    print(f'request.GET: {request.GET}')
    return HttpResponse(f'Question: {quest_id}')


def all_questions_pg(request):
    return HttpResponse('<h1>All questions:</h1>'
                        '<a href = "http://127.0.0.1:8000/">'
                        'Назад')


def slug_question(request, quest_slug):
    if request.POST:
        print(f'request.GET: {request.POST}')
    elif request.GET:
        print(f'request.GET: {request.GET}')
    return HttpResponse(f'Question by slug: {quest_slug}')


def archive(request, year):
    if year > 2025:
        raise Http404()
    print(f'request.GET: {request.GET}')
    return HttpResponse(f'Questions arhcive by year: {year}')


def page_not_found(request, exception):
    return HttpResponseNotFound(
        '<h1><b>Страница не найдена!</b></h1>'
        '<a href = "http://127.0.0.1:8000/">'
        'Назад')
