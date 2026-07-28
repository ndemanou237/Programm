from django.shortcuts import render
from django_q.tasks import async_task
from .tasks import generer_facture_pdf
from django.utils import timezone
import zoneinfo
from datetime import datetime
from .models import Event
from django.core.exceptions import PermissionDenied

# def passer_commande_view(request):
#     commande_id = 1234
#     email = "cliant@gmail.com"
#     async_task('blog.tasks.generer_facture_pdf', commande_id, email)
#     context = {
#         'commande_id': commande_id,
#         'email': email,
#     }
#     return render(request, 'index.html', context)

def passer_commande_view(request):
    commande_id = 1234
    email = "cliant@gmail.com"
    generer_facture_pdf.delay(commande_id, email)
    context = {
        'commande_id': commande_id,
        'email': email,
    }
    return render(request, 'index.html', context)

def home(request):
    return render(request, 'home.html')   

def test(request):
    calcul = 1/0
    return render(request, 'calcul.html') 

# def test2(request):
#     raise PermissionDenied("Vous n'avez pas l'autorisation")   
# 
# def afficher_heure(request):
#     maintenant = timezone.now()
#     return render(request, 'heure.html', {'heure_actuelle': maintenant})     

def create_and_show_event(request):
    douala_tz = zoneinfo.ZoneInfo("Africa/Douala")
    local_dt = datetime(2026, 7, 28, 15, 0, 0, tzinfo=douala_tz)
    event = Event.objects.create(
        title = "conference tech",
        start_time= local_dt
    )
    utc_time = event.start_time
    paris_tz = zoneinfo.ZoneInfo("Europe/Paris")
    paris_time = utc_time.astimezone(paris_tz)

    context = {
        'event': event,
        'utc_time': utc_time,
        'paris_time': paris_time,
    }

    return render(request, 'detail.html', context)