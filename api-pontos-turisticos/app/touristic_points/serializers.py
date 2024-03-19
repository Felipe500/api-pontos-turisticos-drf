from rest_framework import serializers

from app.attractions.serializers import AttractionsSerializer
from app.attractions.models import Attraction
from app.reviews.models import Review

from .models import TouristicPoint


class AddressSerializer2(serializers.Serializer):
    number = serializers.IntegerField()
    district = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    country = serializers.CharField(required=False)
    zip = serializers.IntegerField()
    latitude = serializers.IntegerField(required=False)
    longitude = serializers.IntegerField(required=False)


class TouristicPointSerializer(serializers.ModelSerializer):
    attractions = AttractionsSerializer(many=True, required=False)
    address = AddressSerializer2(write_only=True)
    review = serializers.FloatField(required=False, source='percent_review')
    user_rated = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TouristicPoint
        fields = (
            'id',
            'name',
            'description',
            'photo',
            'approved',
            'attractions',
            'review',
            'total_review',
            'user_rated',
            'address',
            )
        read_only_fields = ['review', 'total_review', 'attractions']

    def get_address(self, obj):
        return AddressSerializer2(obj).data

    def get_list_attractions(self, obj):
        return AttractionsSerializer(obj.attractions, many=True).data

    def get_user_rated(self, obj):
        user_id = self.context.get('user').id
        return Review.objects.filter(user_id=user_id, tourist_spot_id=obj.id).exists()

    @classmethod
    def create_attractions(cls, attractions=[dict], tourist_spot=None):
        for attraction in attractions:
            attraction['tourist_spot'] = tourist_spot
            Attraction.objects.create(**attraction)

    def create(self, validated_data, attractions=[], address=None):
        if 'attractions' in validated_data.keys():
            attractions = validated_data.pop('attractions', [])

        if 'address' in validated_data.keys():
            address = validated_data.pop('address', {})
            for attr, val in address.items():
                validated_data[attr] = val

        new_touristic_point = TouristicPoint.objects.create(**validated_data)

        self.create_attractions(attractions, new_touristic_point)
        
        return new_touristic_point

    def update(self, instance, validated_data):
        if 'attractions' in validated_data.keys():
            validated_data.pop('attractions', [])

        if 'address' in validated_data.keys():
            address = validated_data.pop('address', {})
            for attr, val in address.items():
                validated_data[attr] = val

        return super().update(instance, validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['address'] = AddressSerializer2(instance).data
        return data
