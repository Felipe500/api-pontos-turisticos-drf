from django.db import models
from django.core.validators import RegexValidator

from app.common.models import BaseModel


class Review(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    note = models.PositiveIntegerField(max_length=2, validators=[RegexValidator(r'\b([0-9]|10)\b')])
    tourist_spot = models.ForeignKey('touristic_points.TouristicPoint', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name
