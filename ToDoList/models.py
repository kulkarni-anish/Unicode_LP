
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ToDo(models.Model):
    name        = models.CharField(max_length=50)
    description = models.TextField(null=True)
    status      = models.BooleanField(default=False)
    date        = models.DateTimeField(auto_now=True,auto_now_add=False)
    updates     = models.IntegerField(default=0)
    deadline    = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name


class MyUserModel(AbstractUser):
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    email       = models.EmailField(max_length=60,blank=True)
