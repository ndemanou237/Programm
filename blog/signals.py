from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def mon_premier_signal(sender, instance, created, **kwargs):
    if created:
        print('\n' + "="*50)
        print(f"SIGNAL DECLENCHE: L'utilisateur '{instance.username}' a été crée avec sucess")
        print("="*50 + "\n")