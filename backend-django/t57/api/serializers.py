# from centraal.models import Url
from rest_framework import serializers
from centraal.models import *

# Serializers define the API representation.
class UrlSerializer(serializers.ModelSerializer):
    u_owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Url
        # fields = ['url', 'username', 'email', 'is_staff']
        fields =  '__all__'
        read_only_fields = ('u_trello_card_id', 'u_owner')


# Serializers define the API representation.
class UserProfileSerializer(serializers.ModelSerializer):
    p_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = UserProfile
        # fields = ['url', 'username', 'email', 'is_staff']
        fields =  '__all__'