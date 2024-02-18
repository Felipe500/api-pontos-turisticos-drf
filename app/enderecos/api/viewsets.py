from rest_framework import viewsets
from app.enderecos.models import Endereco
from app.enderecos.api.serializers import EnderecoSerializer


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    