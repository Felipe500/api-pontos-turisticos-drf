from django.db import models
from app.common.models import BaseModel
from app.attractions.models import Attraction
from app.reviews.models import Review
from app.address.models import Address


class TouristicPoint(BaseModel):
    name = models.CharField(max_length=150)
    description = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='tourist_spot', null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def description_complete(self):
        return f'{self.name} - {self.description[:18]}'

    @property
    def attractions(self):
        return Attraction.objects.filter(tourist_spot_id=self.pk)

    @property
    def reviews(self):
        return Review.objects.filter(tourist_spot_id=self.pk)
