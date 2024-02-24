from django.db import models
from django.core.validators import RegexValidator

from app.common.models import BaseModel


class Review(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    note = models.PositiveIntegerField(max_length=2, validators=[RegexValidator(r'\b([1-9]|10)\b')])

    def __str__(self):
        return self.user.name
