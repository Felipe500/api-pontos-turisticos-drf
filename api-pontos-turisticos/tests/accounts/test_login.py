import pytest

from rest_framework.test import APIClient
from rest_framework import status

from django.urls.base import reverse

from .. import constants


@pytest.mark.django_db
class TestAuthenticate:
    def test_login(self, user_1, user_2):
        payload_data = {
            "email": constants.email_user1,
            "password": constants.default_pass
        }

        response = APIClient().post(reverse('accounts:signin'), payload_data)

        assert response.status_code == status.HTTP_200_OK

        data = response.json()

        assert data.get('name') == user_1.name
        assert data.get('email') == user_1.email
        assert len(data.get('token').split('.')) == 3
        assert len(data.get('refresh').split('.')) == 3

    def test_refresh_token(self, user_1):
        response = APIClient().post(reverse('accounts:token_refresh'), {'refresh': user_1.refresh})

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data.get('access').split('.')) == 3

    def test_get_infor(self, user_2):
        client = APIClient()
        client.force_authenticate(user_2)
        client.credentials(HTTP_AUTHORIZATION=f"JWT {user_2.token}")

        response = client.get(reverse('accounts:info'))

        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert data.get('id') == user_2.id
        assert data.get('name') == user_2.name
        assert data.get('email') == user_2.email