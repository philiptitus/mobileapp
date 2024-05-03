from rest_framework import viewsets
from ..models import *
from .serializers import *



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer