from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404


from . import models

# Create your views here.

data_menu = [
    {'page_title': 'Главная', 'page_route': 'home'},
    {'page_title': 'О сайте', 'page_route': 'about'},
]


def index(request) -> HttpResponse:
    questions = models.Question.published.all()
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
    answers = models.Answer.objects.filter(question=quest_id)
    tags = quest_by_id.tags.all()
    data = {
        'title': quest_by_id.title,
        'question_content': quest_by_id.content,
        'quest_autor': quest_by_id.user,
        'question_time': quest_by_id.time_create,
        'answers': answers,
        'create time': quest_by_id.time_create,
        'menu': data_menu,
        'tags': tags,
    }
    return render(request, 'main_app/question.html', data)


def show_tag_questlist(request, tag_slug):
    tag = get_object_or_404(models.TagQuestion, slug=tag_slug)
    questions = tag.tags.filter(is_published=True)
    data = {
        'title': f'Вопросы по теме: {tag.tag}',
        'menu': data_menu,
        'questions': questions,
    }
    return render(request, 'main_app/questions_by_tags.html', data)


def page_not_found(request, exception) -> HttpResponseNotFound:
    return HttpResponseNotFound(
        '<h1><b>Страница не найдена!</b></h1>'
        '<a href = "http://127.0.0.1:8000/">'
        'Назад')
