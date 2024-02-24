from django.db import models


class Attraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    opening_hours = models.TextField()
    minimum_age = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='attraction', null=True, blank=True)
    observation = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.nome
        