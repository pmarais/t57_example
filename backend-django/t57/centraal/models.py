from statistics import mode
from django.db import models

## for importing custom user model
from django.conf import settings
## custom user mdoel import as User
from django.contrib.auth import get_user_model
User = get_user_model()

from .utils import *


# Create your models here.

class UserProfile(models.Model):
    p_user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_profile', on_delete=models.CASCADE, null=True, blank=True)
    p_trello_api_key = models.CharField(max_length=255, default='', blank=True, null=True)
    p_trello_api_secret = models.CharField(max_length=255, default='', blank=True, null=True)
    p_trello_token = models.CharField(max_length=255, default='', blank=True, null=True)
    p_trello_token_secret = models.CharField(max_length=255, default='', blank=True, null=True)
    # p_trello_default_list = models.CharField(max_length=255, default='', blank=True, null=True)

    def __str__(self):
        return "%s => Profile"%(self.p_user)

class Url(models.Model):
    u_owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_urls', on_delete=models.CASCADE, null=True, blank=True)
    u_url = models.CharField(max_length=255, default='', blank=True, null=True)
    u_created = models.DateTimeField(auto_now_add=True)
    u_modified = models.DateTimeField(auto_now=True)
    u_trello_card_id = models.CharField(max_length=255, default='', blank=True, null=True)
    u_snapshot = models.ImageField(upload_to='snapshots', max_length=255)

    def __str__(self):
        return "%s) %s [%s]"%(self.pk, self.u_url, self.u_owner)

    def add_url_to_trello(self):
        tc = TrelloClientClass(self.u_owner)
        trello_list = tc.connect_to_trello_retieve_list()
        card = trello_list.add_card(self.u_url, desc=self.u_url, labels=None, due='null', source=None, position=None, assign=None)
        self.u_trello_card_id = card.id
        self.save()

    def remove_from_trello(self):
        try:
            tc = TrelloClientClass(self.u_owner)
            card = tc.connect_to_trello_retieve_card(str(self.u_trello_card_id))
            card.delete()
        except:
            pass




        

