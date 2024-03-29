from django.db import models
from django.core.validators import RegexValidator

from app.common.models import BaseModel
from .managers import ReviewsManager


class Review(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    note = models.PositiveIntegerField(validators=[RegexValidator(r'\b([1-9]|10)\b')])
    tourist_spot = models.ForeignKey('touristic_points.TouristicPoint', on_delete=models.CASCADE)

    objects = ReviewsManager()

    class Meta:
        unique_together = ['user', 'tourist_spot']

    def __str__(self):
        return self.user.name

