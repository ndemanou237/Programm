from django.shortcuts import render
from django_q.tasks import async_task
from .tasks import generer_facture_pdf

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
