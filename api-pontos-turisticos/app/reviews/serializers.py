from django.db.models import F
from django.core.validators import RegexValidator
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, IntegerField
from rest_framework.serializers import ValidationError
from app.touristic_points.models import TouristicPoint

from .models import Review


class ReviewSerializer(ModelSerializer):
    touristic_point_id = PrimaryKeyRelatedField(
        many=False,
        required=True,
        write_only=True,
        source='tourist_spot',
        queryset=TouristicPoint.objects.all(),
    )
    note = IntegerField(required=True, validators=[RegexValidator(r'\b([0-9]|10)\b')])

    class Meta:
        model = Review
        fields = ['id', 'touristic_point_id', 'user_id', 'text', 'note', 'created_at']
        read_only_fields = ['user_id']

    def create(self, validated_data):
        if Review.objects.filter(user_id=self.context.get('user_id')).exists():
            raise ValidationError({'error': 'evaluation already created'})
        return super().create(validated_data)

    def update(self, instance, validated_data):
        Review.objects.update_review(instance.tourist_spot.id, instance.note, validated_data['note'])
        return super().update(instance, validated_data)
