from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    def __str__(self):
        return f"{self.title} - {self.start_time}"