from health_diary_infrastructure.queries import (
    DjangoGettingSpecificStatisticHistory
)
from .foundation import user
from health_diary_api.models import HealthDiary
import pytest
import datetime


@pytest.fixture()
def diaries(user):
    today = datetime.date.today()
    HealthDiary.objects.bulk_create([
        HealthDiary(user_id=user.id, date=today
                    - datetime.timedelta(0), weigth=100),
        HealthDiary(user_id=user.id, date=today
                    - datetime.timedelta(1), weigth=100),
        HealthDiary(user_id=user.id, date=today
                    - datetime.timedelta(2), weigth=100),
        HealthDiary(user_id=user.id, date=today
                    - datetime.timedelta(3), weigth=100),
        HealthDiary(user_id=user.id, date=today
                    - datetime.timedelta(4), weigth=100),
        HealthDiary(user_id=user.id, date=today
                    - datetime.timedelta(5), weigth=100),
        HealthDiary(user_id=user.id, date=today
                    - datetime.timedelta(6), weigth=100),
    ])


@pytest.fixture()
def query(diaries) -> DjangoGettingSpecificStatisticHistory:
    return DjangoGettingSpecificStatisticHistory()


@pytest.mark.django_db
def test_getting_weigth_history_with_default_number(user, query) -> None:
    results = query.query(user.id, 'weigth')
    assert len(results['values']) == 7


@pytest.mark.django_db
def test_getting_weigth_history_with_non_default_number(user, query) -> None:
    results = query.query(user.id, 'weigth', 4)
    assert len(results['values']) == 4
