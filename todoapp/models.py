from django.db import models
from django.contrib.auth.models import User
import datetime

class Task(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.date.today())
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title