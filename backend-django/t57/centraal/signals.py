from django.db.models.signals import post_save
from django.dispatch import receiver
from centraal.models import Url

from .tasks import add_url_to_trello

@receiver(post_save, sender=Url)
def send_to_trello(sender, instance, created, **kwargs):
    print('post-save')
    if created:
        add_url_to_trello.delay(instance.pk)
