from rest_framework import serializers

from app.atracoes.serializers import AtracaoSerializer
from app.enderecos.serializers import EnderecoSerializer
from app.atracoes.models import Atracao
from app.enderecos.models import Endereco

from .models import TouristSpot


class TouristSpotSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer(read_only=True)
    descricao_completa = serializers.SerializerMethodField()

    class Meta:
        model = TouristSpot
        fields = (
            'id', 'nome', 'descricao', 'aprovado', 'foto', 
            'atracoes', 'comentarios', 'avaliacoes', 'endereco', 'descricao_completa', 
            'descricao_completa2', 'doc_identificacao'
            )
        read_only_fields = ['comentarios', 'avaliacoes']

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        
        endereco = validated_data['endereco']
        del validated_data['endereco']

        ponto = TouristSpot.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)
        
        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.save()
        
        return ponto

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
