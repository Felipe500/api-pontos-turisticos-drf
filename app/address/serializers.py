from rest_framework.serializers import ModelSerializer
from app.address.models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
