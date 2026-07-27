from django.urls import path
from .views import passer_commande_view,home

urlpatterns = [
    path('commander/', passer_commande_view, name='passer_commande'),
    path('', home, name="home")
]
