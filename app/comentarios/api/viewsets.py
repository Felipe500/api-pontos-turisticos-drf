from app.comentarios.models import Comentario
from app.comentarios.api.serializers import ComentarioSerializer
from app.common.view import ViewCommon


class ComentarioViewSet(ViewCommon):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    