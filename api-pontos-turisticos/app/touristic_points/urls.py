from django.urls import path

from .views import ChangePontoTuristicoViewSet, ReadPontoTuristicoViewSet

app_name = "touristic_points"

urlpatterns = [
    path('', ChangePontoTuristicoViewSet.as_view({'post': 'create'}), name='create'),
    path('list', ReadPontoTuristicoViewSet.as_view({'get': 'list'}), name='list'),
    path('view/<int:pk>', ReadPontoTuristicoViewSet.as_view({'get': 'retrieve'}), name='retrieve'),
    path('change/<int:pk>', ChangePontoTuristicoViewSet.as_view({'put': 'update', 'delete': 'destroy'}), name='change')
]
