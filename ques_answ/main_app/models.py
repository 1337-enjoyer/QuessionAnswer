from django.db import models
from django.urls import reverse


class QuestionManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_published=True)


class Question(models.Model):
    title: models.CharField = models.CharField(max_length=255)
    content: models.TextField = models.TextField(blank=True)
    user: models.CharField = models.CharField(max_length=20, default='Гость')
    time_create: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    is_published: models.BooleanField = models.BooleanField(default=True)

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
    answer_time: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    user: models.CharField = models.CharField(max_length=20, default='Гость')
    question: models.ForeignKey = models.ForeignKey(
        Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[0:5]
