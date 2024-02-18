from rest_framework.serializers import ModelSerializer
from app.comentarios.models import Comentario


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['usuario', 'comentario', 'data', 'aprovado']
        