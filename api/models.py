from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.title
