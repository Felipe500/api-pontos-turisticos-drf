import pytest

from rest_framework.test import APIClient
from rest_framework import status
from django.urls.base import reverse


@pytest.mark.django_db
class TestListTouristicPoints:

    def test_update(self, api_client_1, touristic_points_1, touristic_points_2):
        pk_change = touristic_points_1.pk
        payload_data = {
            "name": "ponto turistico 1.1 atualizado",
            "description": "Descrição 1.1",
            "address": {
                "number": 999,
                "district": "district",
                "city": "city",
                "state": "state",
                "country": "state",
                "zip":  909090
            },
        }
        response_retrieve = APIClient().get(reverse('touristic_points:retrieve', kwargs={"pk": pk_change}))

        assert response_retrieve.status_code == status.HTTP_200_OK

        response_change = api_client_1.put(reverse('touristic_points:change', kwargs={"pk": pk_change}), payload_data)
        response_data = response_change.json()

        assert response_data.get('id') == pk_change
        assert response_data.get('name') == payload_data['name']
        assert response_data.get('description') == payload_data['description']
        assert response_data.get('address').get('number') == int(payload_data['address']['number'])
        assert response_data.get('address').get('district') == payload_data['address']['district']
        assert response_data.get('address').get('city') == payload_data['address']['city']
        assert response_data.get('address').get('state') == payload_data['address']['state']
        assert response_data.get('address').get('country') == payload_data['address']['country']
        assert response_data.get('address').get('zip') == payload_data['address']['zip']

    def test_delete(self, api_client_1, touristic_points_1, touristic_points_2):
        pk_delete = touristic_points_2.pk
        response = APIClient().get(reverse('touristic_points:list'))
        response_data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_data.get('count') == 2

        response_delete = api_client_1.delete(reverse('touristic_points:change', kwargs={"pk": pk_delete}))

        response = APIClient().get(reverse('touristic_points:list'))
        response_data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert response_data.get('count') == 1
