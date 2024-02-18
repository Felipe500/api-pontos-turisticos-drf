from app.comentarios.models import Comentario

from app.common.view import ViewCommon

from .serializers import ComentarioSerializer


class ComentarioViewSet(ViewCommon):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
