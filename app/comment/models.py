from django.db import models

from app.common.models import BaseModel


class Comment(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0, editable=False)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, editable=False)
    tourist_spot = models.ForeignKey('touristic_points.TouristicPoint', on_delete=models.CASCADE)
    approved = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user.name)
