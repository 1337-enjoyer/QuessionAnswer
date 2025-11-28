from django.db import models
from django.urls import reverse


class QuestionManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_published=True)


class Question(models.Model):
    title: models.CharField = models.CharField(max_length=255, db_index=True)
    content: models.TextField = models.TextField(blank=True)
    user: models.CharField = models.CharField(
        max_length=20, default='Гость', db_index=True)
    time_create: models.DateTimeField = models.DateTimeField(
        auto_now_add=True, db_index=True)
    is_published: models.BooleanField = models.BooleanField(default=True)
    tags: models.ManyToManyField = models.ManyToManyField(
        'TagQuestion', blank=True, related_name='tags')

    objects = models.Manager()
    published = QuestionManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('question', kwargs={'quest_id': self.pk})


class Answer(models.Model):
    content: models.TextField = models.TextField(blank=False)
    answer_time: models.DateTimeField = models.DateTimeField(
        auto_now_add=True, db_index=True)
    user: models.CharField = models.CharField(
        max_length=20, default='Гость', db_index=True)
    question: models.ForeignKey = models.ForeignKey(
        Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[0:5]


class TagQuestion(models.Model):
    tag: models.CharField = models.CharField(
        max_length=100, db_index=True)
    slug: models.SlugField = models.SlugField(
        max_length=255, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})
