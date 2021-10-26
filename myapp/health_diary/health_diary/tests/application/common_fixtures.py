import pytest
from health_diary.domain.entities import HealthDiary
from health_diary.application.repositories import (
    HealthDiaryRepository,
    )
from unittest.mock import Mock


@pytest.fixture()
def user_id() -> int:
    return 2


@pytest.fixture()
def health_diary(user_id: user_id) -> HealthDiary:
    return HealthDiary(user_id=user_id)


@pytest.fixture()
def diary_repo_mock(health_diary) -> Mock:
    return Mock(spec_set=HealthDiaryRepository, get=Mock(return_value=health_diary))
