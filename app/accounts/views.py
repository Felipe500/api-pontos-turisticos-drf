from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from app.accounts.serializers import SignInSerializer, AccountCreateSerializer, UserInfoSerializer


class LoginAPIView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SignInSerializer

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccountCreateAPIView(generics.CreateAPIView):
    serializer_class = AccountCreateSerializer
    model = serializer_class.Meta.model
    permission_classes = (AllowAny,)

    def post(self, request: Request, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AccountAPIView(generics.GenericAPIView):
    serializer_class = UserInfoSerializer
    model = serializer_class.Meta.model

    def get(self, request: Request) -> Response:
        return Response(self.serializer_class(request.user, context={'request': request}).data)



