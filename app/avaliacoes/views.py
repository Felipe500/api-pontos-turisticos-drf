from app.avaliacoes.models import Avaliacao

from app.common.view import ViewCommon

from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ViewCommon):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
