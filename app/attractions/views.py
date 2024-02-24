from django_filters.rest_framework import DjangoFilterBackend

from app.atracoes.models import Atracao
from app.common.view import ViewCommon

from .serializers import AtracaoSerializer


class AtracaoViewSet(ViewCommon):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'descricao']