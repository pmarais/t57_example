from statistics import mode
from django.db import models

from .utils import *
from centraal.tasks import add_url_to_trello

# Create your models here.

class Url(models.Model):
    u_url = models.CharField(max_length=255, default='', blank=True, null=True)
    u_created = models.DateTimeField(auto_now_add=True)
    u_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s) %s"%(self.pk, self.u_url)

    def add_url_to_trello(self):
        trello_list = connect_to_trello_retieve_list()
        trello_list.add_card(self.u_url, desc=self.u_url, labels=None, due='null', source=None, position=None, assign=None)

        

