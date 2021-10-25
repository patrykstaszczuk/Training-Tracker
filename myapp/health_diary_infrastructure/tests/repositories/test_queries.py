from health_diary_infrastructure.queries import (
    DjangoGettingDailyStatistics
)
from .foundation import user
from health_diary_api.models import HealthDiary
import pytest
import datetime


@pytest.fixture()
def diary(user) -> HealthDiary:
    today = datetime.date.today()
    return HealthDiary.objects.create(
        user_id=user.id,
        date=today,
        weigth=100)


@pytest.fixture()
def yesterday_diary(user) -> HealthDiary:
    yesterday = datetime.date.today() - datetime.timedelta(1)
    return HealthDiary.objects.create(
        user_id=user.id,
        date=yesterday,
        weigth=200)


@pytest.fixture()
def query(diary, yesterday_diary) -> DjangoGettingDailyStatistics:
    return DjangoGettingDailyStatistics()


@pytest.mark.django_db
def test_retrieve_daily_statistics(user, query) -> None:
    diary = query.query(user_id=user.id)
    assert diary['user_id'] == user.id
    assert diary['weigth'] == 100


@pytest.mark.django_db
def test_retrieve_daily_statistics_for_given_day(user, query) -> None:
    today = datetime.date.today()
    todays_diary = query.query(user_id=user.id, date=today)
    assert todays_diary['date'] == today
