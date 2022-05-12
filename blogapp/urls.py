from django.urls import path
from .views import *

urlpatterns = [
    path('', blog),
    path('maqola/', maqola),
    path('about/', about),
    path('interviyu/', interviyu),
    ]