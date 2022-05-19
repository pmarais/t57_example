from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from centraal.models import *
from .serializers import *

# ViewSets define the view behavior.
class UrlViewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all().order_by('-pk')
    serializer_class = UrlSerializer