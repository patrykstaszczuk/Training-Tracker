from health_diary_infrastructure.queries import (
    DjangoGettingSpecificStatisticHistory
)
from .foundation import user
from health_diary_api.models import HealthDiary
import pytest
import datetime


@pytest.fixture()
def diaries(user) -> HealthDiary:
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
