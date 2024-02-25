from rest_framework import serializers

from app.attractions.serializers import AttractionSerializer
from app.address.serializers import AddressSerializer
from app.attractions.models import Attraction
from app.address.models import Address

from .models import TouristicPoint


class TouristicPointSerializer(serializers.ModelSerializer):
    attractions = AttractionSerializer(many=True, required=False)
    address = AddressSerializer(read_only=True)

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

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Attraction.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data, atracoes=[], endereco=None):
        if 'attractions' in validated_data.keys():
            atracoes = validated_data['attractions']
            del validated_data['atracoes']
        if validated_data.get('address', None):
            endereco = validated_data.get('address', None)
            validated_data.pop("address")

        ponto = TouristicPoint.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        if endereco:
            address = Address.objects.create(**endereco)
            ponto.endereco = address
        ponto.save()
        
        return ponto
