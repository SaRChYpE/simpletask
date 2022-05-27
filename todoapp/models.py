from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=255)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)