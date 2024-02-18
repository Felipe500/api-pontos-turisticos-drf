from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from app.atracoes.models import Atracao
from app.atracoes.api.serializers import AtracaoSerializer


class AtracaoViewSet(viewsets.ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'descricao']

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
