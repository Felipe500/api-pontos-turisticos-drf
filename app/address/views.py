from app.address.models import Address
from app.common.view import ViewCommon

from .serializers import AddressSerializer


class AddressViewSet(ViewCommon):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
