import time
from celery import shared_task

@shared_task
def generer_facture_pdf(commande_id, email_client):
    print(f"Debut de la generation du pdf pour la commande #{commande_id}...")
    #simulation 
    time.sleep(5)
    print(f"Facture envoyé avec succes à {email_client} !")