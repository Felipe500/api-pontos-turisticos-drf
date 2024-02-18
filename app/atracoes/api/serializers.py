from rest_framework.serializers import ModelSerializer
from app.atracoes.models import Atracao


class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('id', 'nome', 'descricao', 'horario_func', 'idade_minima', 'foto', 'observacoes')
