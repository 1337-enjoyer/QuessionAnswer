from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    count_answers = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    