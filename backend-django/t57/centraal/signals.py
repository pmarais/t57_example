from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from centraal.models import Url

from .tasks import add_url_to_trello, remove_url_from_trello

@receiver(post_save, sender=Url)
def send_to_trello(sender, instance, created, **kwargs):
    print('post-save')
    if created:
        add_url_to_trello.delay(instance.pk)

@receiver(pre_delete, sender=Url)
def delete_from_trello(sender, instance, **kwargs):
    print('pre-delete')
    remove_url_from_trello.delay(instance.u_trello_card_id)
