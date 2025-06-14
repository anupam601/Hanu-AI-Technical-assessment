from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
