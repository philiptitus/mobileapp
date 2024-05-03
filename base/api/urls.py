from rest_framework import routers
from ..models import *
from .views import *
from django.urls import *


router = routers.DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path ('', include(router.urls))
]