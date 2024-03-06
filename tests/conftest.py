import pytest
from rest_framework.test import APIClient

from django.conf import settings
from django.utils import timezone

from app.accounts.models import User
from app.reviews.models import Review
from app.comment.models import Comment
from app.attractions.models import Attraction
from app.touristic_points.models import TouristicPoint

from .constants import email_user1, email_user2, default_pass, touristic_points1, touristic_points2


@pytest.fixture
def user_admin(db) -> User:
    _subscriber = User.objects.create_user(**{'name': 'user1', 'email': email_user1, 'password': default_pass})
    return _subscriber


@pytest.fixture
def user_1(db) -> User:
    _subscriber = User.objects.create_user(**{'name': 'user1', 'email': email_user1, 'password': default_pass})
    return _subscriber


@pytest.fixture
def user_2(db) -> User:
    return User.objects.create_user(**{'name': 'user2', 'email': email_user2, 'password': default_pass})


@pytest.fixture
def api_client_1(user_1):
    client = APIClient()
    client.force_authenticate(user_1)
    client.credentials(HTTP_AUTHORIZATION=f"JWT {user_1.token}")
    return client


@pytest.fixture
def touristic_points_1() -> TouristicPoint:
    return TouristicPoint.objects.create(**touristic_points1)


@pytest.fixture
def touristic_points_2() -> TouristicPoint:
    return TouristicPoint.objects.create(**touristic_points2)


@pytest.fixture
def review_1(touristic_points_1) -> Review:
    return Review.objects.create(**{"touristic_point": touristic_points_1, "text": "BOA", "note": 7})


@pytest.fixture
def review_1(touristic_points_1) -> Review:
    return Review.objects.create(**{"touristic_point": touristic_points_1, "text": "BOA", "note": 7})
