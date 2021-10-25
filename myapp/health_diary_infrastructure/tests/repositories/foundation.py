""" This module create common fixtures for tests """
import pytest
from django.contrib.auth.models import User


@pytest.fixture()
def user() -> User:
    return User.objects.create(username='test', password='testpass')
