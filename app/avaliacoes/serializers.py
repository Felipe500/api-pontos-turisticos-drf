from rest_framework.serializers import ModelSerializer
from app.avaliacoes.models import Avaliacao


class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id', 'user', 'comentario', 'nota', 'data']
        