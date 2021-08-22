
from django.db import models
from django.utils import timezone
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
