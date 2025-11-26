from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
