from rest_framework import viewsets
from app.comentarios.models import Comentario
from app.comentarios.api.serializers import ComentarioSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    