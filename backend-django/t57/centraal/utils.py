from trello import TrelloClient

# export TRELLO_API_KEY='559d3dd5af1db257129718c461bbc14a'
# export TRELLO_API_SECRET='57d1c8606c7f43dede2b295f7abbd7aaacf439d3b9573a5099aaec5938eb4f1c'
# export TRELLO_EXPIRATION'never'

from .creds import credentials

def connect_to_trello_retieve_list():
        client = TrelloClient(
            api_key = credentials['api_key'],
            api_secret = credentials['api_secret'],
            token = credentials['token'],
            token_secret = credentials['token_secret']
        )

        pilot_list = client.get_list(credentials['pilot_board'])
        return pilot_list

def connect_to_trello_retieve_card(card_id):
        client = TrelloClient(
            api_key = credentials['api_key'],
            api_secret = credentials['api_secret'],
            token = credentials['token'],
            token_secret = credentials['token_secret']
        )

        card = client.get_card(card_id)
        return card

def connect_to_trello_retieve_client():
        client = TrelloClient(
            api_key = credentials['api_key'],
            api_secret = credentials['api_secret'],
            token = credentials['token'],
            token_secret = credentials['token_secret']
        )

        return client