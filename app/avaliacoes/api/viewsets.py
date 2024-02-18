from rest_framework import viewsets
from app.avaliacoes.models import Avaliacao
from app.avaliacoes.api.serializers import AvaliacaoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    