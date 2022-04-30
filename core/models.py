from django.db import models

# Create your models here.
class avgTemp(models.Model):
    date = models.DateField()
    average = models.FloatField()

    class Meta:
        ordering = ('date',)

class avgRain(models.Model):
    date = models.DateField()
    average = models.FloatField()

    class Meta:
        ordering = ('date',) 