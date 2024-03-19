from django_filters.rest_framework import DjangoFilterBackend

from app.attractions.models import Attraction
from app.common.view import ViewCommon

from .serializers import AttractionSerializer


class AtracaoViewSet(ViewCommon):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description']
