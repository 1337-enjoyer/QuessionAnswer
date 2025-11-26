from django.db import models
from django.urls import reverse


class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    count_answers = models.IntegerField(default=0)
    is_published: models.BooleanField = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('question', kwargs={'quest_id': self.pk})
