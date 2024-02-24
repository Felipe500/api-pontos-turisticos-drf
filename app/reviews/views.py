from app.avaliacoes.models import Review
from app.common.view import ViewCommon

from .serializers import ReviewSerializer


class AvaliacaoViewSet(ViewCommon):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
