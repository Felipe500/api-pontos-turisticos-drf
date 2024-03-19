import pytest

from rest_framework.test import APIClient
from rest_framework import status
from django.urls.base import reverse


@pytest.mark.django_db
class TestListTouristicPoints:

    def test_list(self, api_client_1, touristic_points_1, touristic_points_2):
        response = APIClient().get(reverse('touristic_points:list'))
        response_data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_data.get('count') == 2

    def test_search(self, api_client_1, touristic_points_1, touristic_points_2):
        search = 'carro'
        response = APIClient().get(reverse('touristic_points:list') + f'?search={search}')
        response_data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_data.get('count') == 0

        search = 'barragem'
        response = APIClient().get(reverse('touristic_points:list') + f'?search={search}')
        response_data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_data.get('count') == 1

        search = 'ponto turistico'
        response = APIClient().get(reverse('touristic_points:list') + f'?search={search}')
        response_data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_data.get('count') == 2
