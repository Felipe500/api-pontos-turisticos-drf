from rest_framework import serializers

from app.core.models import PontoTuristico, DocIdentificacao
from app.atracoes.api.serializers import AtracaoSerializer
from app.enderecos.api.serializers import EnderecoSerializer
from app.atracoes.models import Atracao
from app.enderecos.models import Endereco


class DocIdentificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer(read_only=True)
    descricao_completa = serializers.SerializerMethodField()
    doc_identificacao = DocIdentificacaoSerializer()


    class Meta:
        model = PontoTuristico
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

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)
        
        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)
        
        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.doc_identificacao = doci

        ponto.save()
        
        return ponto

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
