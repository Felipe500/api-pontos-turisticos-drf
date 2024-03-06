import pytest

from rest_framework.test import APIClient
from rest_framework import status
from django.urls.base import reverse

from app.common.messages import DUPLICATION_EMAIL

from .. import constants


@pytest.mark.django_db
class TestAccounts2:

    def test_create_user(self, user_1):
        payload_data = {
            'name': 'Maria Neves',
            'email': 'maria@gmail.com.br',
            'password': constants.default_pass
        }

        response = APIClient().post(reverse('accounts:accounts'), payload_data)

        assert response.status_code == status.HTTP_201_CREATED
        response_data = response.data

        assert response_data.get('name') == payload_data.get('name')
        assert response_data.get('email') == payload_data.get('email')

    def test_error_duplicate_email(self, user_1):
        payload_data = {
            'name': user_1.name,
            'email': user_1.email,
            'password': constants.default_pass
        }

        response = APIClient().post(reverse('accounts:accounts'), payload_data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

        response_data = response.json()

        assert response_data.get('email') == DUPLICATION_EMAIL
