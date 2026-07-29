from django.urls import path
from .views import page_context

urlpatterns = [
    path('context/', page_context, name='context' )
]
