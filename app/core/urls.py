from django.urls import path

from .api.viewsets import PontoTuristicoViewSet

urlpatterns = [
    path('', PontoTuristicoViewSet.as_view({'post': 'create'}), name='criar_pontos_turisticos'),
    path('list', PontoTuristicoViewSet.as_view({'post': 'create'}), name='listar_pontos_turistico'),
    path('<int:pk>', PontoTuristicoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='ponto_turistico'),
]
