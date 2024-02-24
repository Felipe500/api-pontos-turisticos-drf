from django.urls import path

from .views import  AvaliacaoViewSet


urlpatterns = [
    path('', AvaliacaoViewSet.as_view({'post': 'create'}), name='criar_avaliacao'),
    path('list', AvaliacaoViewSet.as_view({'get': 'list'}), name='listar_avaliacoes'),
    path('<int:pk>', AvaliacaoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='avaliacao'),
]
