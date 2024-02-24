import re

from django.core.validators import RegexValidator
from rest_framework.serializers import ModelSerializer, ValidationError, RegexField, IntegerField
from app.reviews.models import Review


class ReviewSerializer(ModelSerializer):
    note = IntegerField(required=True, validators=[RegexValidator(r'\b([0-9]|10)\b')])

    class Meta:
        model = Review
        fields = ['id', 'user', 'text', 'note', 'created_at']


