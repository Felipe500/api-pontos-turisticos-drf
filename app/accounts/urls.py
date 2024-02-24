from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    LoginAPIView, AccountAPIView, AccountCreateAPIView
)

urlpatterns = [
    path('', AccountCreateAPIView.as_view(), name='user_create'),
    path('info', AccountAPIView.as_view(), name='info'),
    path('signin', LoginAPIView.as_view(), name='signin'),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
]
