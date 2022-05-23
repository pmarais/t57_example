from trello import TrelloClient

# export TRELLO_API_KEY='559d3dd5af1db257129718c461bbc14a'
# export TRELLO_API_SECRET='57d1c8606c7f43dede2b295f7abbd7aaacf439d3b9573a5099aaec5938eb4f1c'
# export TRELLO_EXPIRATION'never'

# from .creds import credentials

# def connect_to_trello_retieve_list():
#         client = TrelloClient(
#             api_key = credentials['api_key'],
#             api_secret = credentials['api_secret'],
#             token = credentials['token'],
#             token_secret = credentials['token_secret']
#         )

#         pilot_list = client.get_list(credentials['pilot_board'])
#         return pilot_list

# def connect_to_trello_retieve_card(card_id):
#         client = TrelloClient(
#             api_key = credentials['api_key'],
#             api_secret = credentials['api_secret'],
#             token = credentials['token'],
#             token_secret = credentials['token_secret']
#         )

#         card = client.get_card(card_id)
#         return card

# def connect_to_trello_retieve_client():
#         client = TrelloClient(
#             api_key = credentials['api_key'],
#             api_secret = credentials['api_secret'],
#             token = credentials['token'],
#             token_secret = credentials['token_secret']
#         )

#         return client


##################
## Model linked ##
##################
class TrelloClientClass:

    def __init__(self, user):
        self.user = user
        self.client = self.__get_trello_client()

    def __get_trello_client(self):
        client = TrelloClient(
                api_key = self.user.user_profile.p_trello_api_key,
                api_secret = self.user.user_profile.p_trello_api_secret,
                token = self.user.user_profile.p_trello_token,
                token_secret = self.user.user_profile.p_trello_token_secret
            )
        return client

    def connect_to_trello_retieve_list(self):
            pilot_list = self.client.get_list(self.user.user_profile.p_trello_default_list)
            return pilot_list

    def connect_to_trello_retieve_card(self, card_id):
            card = self.client.get_card(card_id)
            return card

    def connect_to_trello_retieve_client(self):
            return self.client