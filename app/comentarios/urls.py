from django.urls import path

from .views import ComentarioViewSet


urlpatterns = [
    path('', ComentarioViewSet.as_view({'post': 'create'}), name='criar_comentario'),
    path('list', ComentarioViewSet.as_view({'get': 'list'}), name='listar_comentarios'),
    path('<int:pk>', ComentarioViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comentario'),
]
