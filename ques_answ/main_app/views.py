from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):  # HttpRequest
    return HttpResponse('Ответы на вопросы')


def question(request, quest_id):
    return HttpResponse(f'Question: {quest_id}')


def slug_question(request, quest_slug):
    return HttpResponse(f'Question by slug: {quest_slug}')
