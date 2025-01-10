from django.db import models
from django.contrib.auth.models import User


class Codigo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=6, default=0)