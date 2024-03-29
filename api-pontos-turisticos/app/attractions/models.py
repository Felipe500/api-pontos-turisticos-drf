from django.db import models

from app.common.models import BaseModel


class Attraction(BaseModel):
    name = models.CharField(max_length=150)
    description = models.TextField()
    opening_hours = models.TextField()
    minimum_age = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='attraction', null=True, blank=True)
    observation = models.CharField(max_length=150, null=True, blank=True)
    tourist_spot = models.ForeignKey('touristic_points.TouristicPoint', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
        