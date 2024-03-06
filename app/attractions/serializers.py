from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from app.touristic_points.models import TouristicPoint

from .models import Attraction


class AttractionSerializer(ModelSerializer):
    touristic_point = PrimaryKeyRelatedField(
        many=False,
        required=True,
        write_only=True,
        source='tourist_spot',
        queryset=TouristicPoint.objects.all(),
    )

    class Meta:
        model = Attraction
        fields = ('id', 'touristic_point', 'name', 'description', 'opening_hours', 'minimum_age', 'photo', 'observation')


class AttractionsSerializer(ModelSerializer):
    class Meta:
        model = Attraction
        fields = ('id', 'name', 'description', 'opening_hours', 'minimum_age', 'photo', 'observation')
