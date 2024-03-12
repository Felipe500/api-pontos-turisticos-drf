import pytest

from rest_framework.test import APIClient
from rest_framework import status
from django.urls.base import reverse


@pytest.mark.django_db
class TestTouristicPoints:

    def test_create(self, api_client_1, touristic_points_1, touristic_points_2):
        payload_data = {
            "name": "ponto turistico 3",
            "description": "Descrição ponto turistico 3.",
            "address": {
                "number": 789,
                "district": "sao bernados",
                "city": "teresina",
                "state": "Piaui",
                "country": "Brasil",
                "zip": 77777
            }
        }

        response_create = api_client_1.post(reverse('touristic_points:create'), payload_data, format="json")
        response_data = response_create.json()

        assert response_create.status_code == status.HTTP_201_CREATED

        pk = response_data.get('id', 0)
        response_retrieve = APIClient().get(reverse('touristic_points:retrieve', kwargs={"pk": pk}))
        response_data = response_retrieve.json()

        assert response_retrieve.status_code == status.HTTP_200_OK
        assert response_data.get('name') == payload_data['name']
        assert response_data.get('description') == payload_data['description']
        assert response_data.get('address').get('number') == payload_data['address']['number']
        assert response_data.get('address').get('district') == payload_data['address']['district']
        assert response_data.get('address').get('city') == payload_data['address']['city']
        assert response_data.get('address').get('state') == payload_data['address']['state']
        assert response_data.get('address').get('country') == payload_data['address']['country']
        assert response_data.get('address').get('zip') == payload_data['address']['zip']
