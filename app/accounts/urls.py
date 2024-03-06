from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    LoginAPIView, AccountAPIView, AccountCreateAPIView
)

app_name = 'accounts'

urlpatterns = [
    path('', AccountCreateAPIView.as_view(), name='accounts'),
    path('info', AccountAPIView.as_view(), name='info'),
    path('signin', LoginAPIView.as_view(), name='signin'),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
]
