from django.contrib.auth import authenticate
from rest_framework import serializers

from app.common.messages import DUPLICATION_EMAIL, INVALID_PASSWORD_OR_USER

from .models import User, Customer


class AccountCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ["name", "email", "phone", "country", "password", "token", "created_at"]
        read_only_fields = ["token", "created_at"]

    def create(self, validated_data: dict):
        validated_data["request"] = self.context["request"]

        if self.Meta.model.objects.filter(email=validated_data.get("email")).exists():
            raise serializers.ValidationError({"email": DUPLICATION_EMAIL})
        user = self.Meta.model.objects.create_user(**validated_data)
        return user


class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs: dict):
        request = self.context.get('request')
        print(attrs)
        user = authenticate(request, **attrs)

        if not user:
            raise serializers.ValidationError({'message': INVALID_PASSWORD_OR_USER})
        self.user = user
        return user

    @property
    def data(self) -> dict:
        return {
            'id': self.user.id,
            'name': self.user.name,
            'email': self.user.email,
            'phone': self.user.phone,
            'token': self.user.token,
            'refresh': self.user.refresh,
            'created_at': self.user.created_at,
            'last_login': self.user.last_login,
        }


class UserInfoSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'email', 'refresh', 'created_at', 'last_login']
