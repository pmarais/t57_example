from statistics import mode
from django.db import models

from .utils import *


# Create your models here.

class Url(models.Model):
    u_url = models.CharField(max_length=255, default='', blank=True, null=True)
    u_created = models.DateTimeField(auto_now_add=True)
    u_modified = models.DateTimeField(auto_now=True)
    u_trello_card_id = models.CharField(max_length=255, default='', blank=True, null=True)

    def __str__(self):
        return "%s) %s"%(self.pk, self.u_url)

    def add_url_to_trello(self):
        trello_list = connect_to_trello_retieve_list()
        card = trello_list.add_card(self.u_url, desc=self.u_url, labels=None, due='null', source=None, position=None, assign=None)
        self.u_trello_card_id = card.id
        self.save()

    def remove_from_trello(self):
        try:
            card = connect_to_trello_retieve_card(str(self.u_trello_card_id))
            card.delete()
        except:
            pass




        

