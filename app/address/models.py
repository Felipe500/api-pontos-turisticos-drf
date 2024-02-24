from django.db import models


class Address(models.Model):
    complement = models.CharField(max_length=150, null=True, blank=True)
    number = models.CharField(max_length=5)
    district = models.CharField(max_length=32)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=70)
    zip = models.CharField(max_length=9)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.complement}'
