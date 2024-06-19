from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    # ... autres champs
    date = models.DateField()
    class Meta:
        app_label = 'pluvieux'
