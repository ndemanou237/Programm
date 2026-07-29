from datetime import datetime

def infos_globales(request):
    return {
        'NOM_DU_SITE': 'Mon Super Site',
        'ANNEE_ACTUELLE': datetime.now().year,
        'EMAIL_CONTACT': 'contact@monsite.com'
    }