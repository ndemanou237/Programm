from django.urls import path
from .views import passer_commande_view,home,test,create_and_show_event

urlpatterns = [
    path('commander/', passer_commande_view, name='passer_commande'),
    path('', home, name="home"),
    path('test/', test),
    # path('test2/', test2)
    path('date/', create_and_show_event)
]
