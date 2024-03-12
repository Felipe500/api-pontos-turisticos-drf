from django.db import models
from app.common.models import BaseModel
from app.attractions.models import Attraction


class TouristicPoint(BaseModel):
    name = models.CharField(max_length=150)
    description = models.TextField()
    photo = models.ImageField(upload_to='tourist_spot', null=True, blank=True)
    approved = models.BooleanField(default=False)
    complement = models.CharField(max_length=150, null=True, blank=True)
    number = models.CharField(max_length=5, null=True, blank=True)
    district = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=70, default='Brasil')
    zip = models.CharField(max_length=9, null=True, blank=True)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    users_reviews = models.IntegerField(default=0)
    total_review = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def description_complete(self):
        return f'{self.name} - {self.description[:18]}'

    @property
    def attractions(self):
        return Attraction.objects.filter(tourist_spot_id=self.pk)

    @property
    def percent_review(self):
        if self.total_review < 1:
            self.total_review += 1
        if self.users_reviews < 1:
            self.users_reviews += 1
        return float(self.total_review / self.users_reviews)
