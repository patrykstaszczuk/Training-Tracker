import pytest
import datetime
from unittest.mock import Mock, patch
from .common_fixtures import (
    user_id,
    health_diary,
    diary_repo_mock,
)
from health_diary.application.use_cases import (
    DeletingMealFromDiary,
    DeletingMealFromDiaryInputDto,
)


@pytest.fixture()
def input_dto() -> DeletingMealFromDiaryInputDto:
    return DeletingMealFromDiaryInputDto(
        user_id=1,
        date=datetime.date.today(),
        meal_ids=[1, ],
    )


@pytest.fixture()
def deleting_meal_uc(diary_repo_mock) -> DeletingMealFromDiary:
    return DeletingMealFromDiary(diary_repo_mock)


def test_load_diary_using_user_id_and_date(
    deleting_meal_uc: DeletingMealFromDiary,
    diary_repo_mock: Mock,
    input_dto: DeletingMealFromDiaryInputDto,
) -> None:
    date = datetime.date.today()
    deleting_meal_uc.execute(input_dto)
    diary_repo_mock.get.assert_called_once_with(input_dto.user_id, date)


def test_save_health_diary(
    deleting_meal_uc: DeletingMealFromDiary,
    input_dto: DeletingMealFromDiaryInputDto
) -> None:

    with patch('health_diary.domain.entities.HealthDiary.remove_meals') as mock:
        deleting_meal_uc.execute(input_dto)
    mock.assert_called_once_with(input_dto.meal_ids)
