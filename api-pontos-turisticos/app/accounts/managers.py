from django.http import HttpRequest
from django.contrib.auth.models import BaseUserManager
from app.common.utils import get_ip_and_agent
from app.common.choices import TYPE_USER


class UserManager(BaseUserManager):
    def add_ip_agent(self, user, request: HttpRequest) -> None:
        if request:
            data = get_ip_and_agent(request)
            user.register_ip = data.get('ip')
            user.register_agent = data.get('agent')

    def create_user(self, email: str, password: str = None, **kwargs: dict):
        request = None
        if 'request' in kwargs:
            request = kwargs.pop('request')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        self.add_ip_agent(user, request)
        user.type = TYPE_USER.customer
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs: dict):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.type = TYPE_USER.admin
        user.save(using=self._db)
        return user
