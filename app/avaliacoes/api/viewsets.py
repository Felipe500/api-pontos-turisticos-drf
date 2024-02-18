from app.avaliacoes.models import Avaliacao
from app.avaliacoes.api.serializers import AvaliacaoSerializer
from app.common.view import ViewCommon


class AvaliacaoViewSet(ViewCommon):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    