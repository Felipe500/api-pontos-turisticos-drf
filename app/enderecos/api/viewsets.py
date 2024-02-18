from app.enderecos.models import Endereco
from app.enderecos.api.serializers import EnderecoSerializer
from app.common.view import ViewCommon


class EnderecoViewSet(ViewCommon):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    