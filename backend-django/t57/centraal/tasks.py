# Create your tasks here

from celery import shared_task

# add_url_to_trello.delay(url.pk)
@shared_task
def add_url_to_trello(url_pk):
    from centraal.models import Url
    url = Url.objects.get(pk=url_pk)
    url.add_url_to_trello()
    