from app.enderecos.models import Endereco

from app.common.view import ViewCommon

from .serializers import EnderecoSerializer


class EnderecoViewSet(ViewCommon):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
