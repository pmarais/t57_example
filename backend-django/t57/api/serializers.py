from centraal.models import Url
from rest_framework import serializers

# Serializers define the API representation.
class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        # fields = ['url', 'username', 'email', 'is_staff']
        fields =  '__all__'