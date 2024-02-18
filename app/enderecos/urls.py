from django.urls import path

from .api.viewsets import EnderecoViewSet


urlpatterns = [
    path('', EnderecoViewSet.as_view({'post': 'create'}), name='criar_endereco'),
    path('list', EnderecoViewSet.as_view({'post': 'create'}), name='listar_enderecos'),
    path('<int:pk>', EnderecoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='endereco'),
]
