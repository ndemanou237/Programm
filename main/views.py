from django.shortcuts import render
from rest_framework import viewsets
from .models import Tache
from .serializers import TacheSerializer

def page_context(request):
    return render(request, 'context.html')

class TacheViewSet(viewsets.ModelViewSet):
    queryset = Tache.objects.all()
    serializer_class = TacheSerializer    
