from django.urls import path

from .views import ReviewViewSet, ListReviewViewSet


urlpatterns = [
    path('', ReviewViewSet.as_view({'post': 'create'}), name='create_review'),
    path('<int:pk>', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='review'),
    path('list', ListReviewViewSet.as_view({'get': 'list'}), name='list_review'),
]
