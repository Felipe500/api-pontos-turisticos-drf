from django.urls import path

from .views import AddressViewSet


urlpatterns = [
    path('', AddressViewSet.as_view({'post': 'create'}), name='criar_endereco'),
    path('list', AddressViewSet.as_view({'get': 'list'}), name='listar_enderecos'),
    path('<int:pk>', AddressViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='endereco'),
]
