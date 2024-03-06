from rest_framework import serializers

from app.attractions.serializers import AttractionsSerializer
from app.address.serializers import AddressSerializer
from app.attractions.models import Attraction
from app.address.models import Address

from .models import TouristicPoint


class TouristicPointSerializer(serializers.ModelSerializer):
    attractions = AttractionsSerializer(many=True, required=False)
    address = AddressSerializer(required=True)

    class Meta:
        model = TouristicPoint
        fields = (
            'id',
            'name',
            'description',
            'photo',
            'approved',
            'attractions',
            'reviews',
            'address',
            )
        read_only_fields = ['reviews']

    def get_list_attractions(self, obj):
        return AttractionsSerializer(obj.attractions, many=True).data

    def create_attractions(self, atracoes, ponto):
        for atracao in atracoes:
            atracao['tourist_spot'] = ponto
            Attraction.objects.create(**atracao)

    def create(self, validated_data, attractions=[], address=None):
        print('create')
        print(validated_data.keys())
        if 'attractions' in validated_data.keys():
            attractions = validated_data['attractions']
            print(attractions)
            del validated_data['attractions']
        if 'address' in validated_data.keys():
            print('address')
            address = validated_data.get('address', None)
            validated_data.pop("address")

        new_touristic_point = TouristicPoint.objects.create(**validated_data)
        self.create_attractions(attractions, new_touristic_point)

        if address:
            print(address)
            address = Address.objects.create(**address)
            new_touristic_point.address = address

        new_touristic_point.save()
        
        return new_touristic_point
