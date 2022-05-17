from statistics import mode
from django.db import models

# Create your models here.

class Url(models.Model):
    u_url = models.CharField(max_length=255, default='', blank=True, null=True)
    u_created = models.DateTimeField(auto_now_add=True)
    u_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s) %s"%(self.pk. self.u_url)

