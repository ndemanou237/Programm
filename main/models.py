from django.db import models

class Tache(models.Model):
    titre = models.CharField(max_length=100)
    completee = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
