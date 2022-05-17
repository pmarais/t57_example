from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from centraal.models import *
from .serializers import *

# ViewSets define the view behavior.
class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer