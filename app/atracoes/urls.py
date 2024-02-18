from django.urls import path

from .api.viewsets import AtracaoViewSet

urlpatterns = [
    path('', AtracaoViewSet.as_view({'post': 'create'}), name='criar_atracao'),
    path('list', AtracaoViewSet.as_view({'post': 'create'}), name='listar_atracoes'),
    path('<int:pk>', AtracaoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='atracao'),
]
