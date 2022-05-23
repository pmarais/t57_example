# Create your tasks here

from celery import shared_task
import os

# add_url_to_trello.delay(url.pk)
@shared_task
def add_url_to_trello(url_pk):
    from centraal.models import Url
    url = Url.objects.get(pk=url_pk)
    os.system('shot-scraper %s -o ./images/%s.jpg --retina'%(url.u_url, url_pk))
    url.add_url_to_trello()

# add_url_to_trello.delay(url.pk)
@shared_task
def remove_url_from_trello(user_pk, u_trello_card_id):
    # from centraal.utils import connect_to_trello_retieve_card
    # card = connect_to_trello_retieve_card(u_trello_card_id)
    # card.delete()
    from centraal.models import User
    from centraal.utils import TrelloClientClass
    user = User.objects.get(pk=user_pk)
    tc = TrelloClientClass(user)
    card = tc.connect_to_trello_retieve_card(u_trello_card_id)
    card.delete()
    