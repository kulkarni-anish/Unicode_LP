
from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
class ToDo(models.Model):
    name        = models.CharField(max_length=50)
    description = models.TextField(null=True)
    status      = models.BooleanField(default=False)
    date        = models.DateTimeField(auto_now=True,auto_now_add=False)
    updates     = models.IntegerField(default=0)
    deadline    = models.DateTimeField(default=timezone.now)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=None)


    def __str__(self):
        return self.name
