from health_diary_infrastructure.queries import (
    DjangoGettingDailyStatistics
)
from django.contrib.auth.models import User
from health_diary_api.models import HealthDiary
import pytest


@pytest.fixture()
def user() -> User:
    return User.objects.create(username='test', password='testpass')


@pytest.fixture()
def diary(user) -> HealthDiary:
    return HealthDiary.objects.create(user_id=user.id, weigth=100)


@pytest.fixture()
def query(diary) -> DjangoGettingDailyStatistics:
    return DjangoGettingDailyStatistics()


@pytest.mark.django_db
def test_retrieve_daily_statistics(user, query) -> None:
    diary = query.query(user_id=user.id)
    assert diary['user_id'] == user.id
    assert diary['weigth'] == 100
