import datetime
import pytest
from health_diary.application.use_cases import(
    AddingMealToDiary,
    AddingMealToDiaryInputdto,
)
from health_diary.domain.entities import HealthDiary
from unittest.mock import Mock, patch
from .common_fixtures import (
    user_id,
    diary_repo_mock,
    health_diary,
)


@pytest.fixture()
def add_meal_uc(diary_repo_mock) -> AddingMealToDiary:
    return AddingMealToDiary(diary_repo_mock)


@pytest.fixture()
def input_dto(user_id) -> AddingMealToDiaryInputdto:
    return AddingMealToDiaryInputdto(
            creator_id=user_id,
            date=datetime.date.today(),
            meals=[
                {"name": 'test dishs',
                 "calories": 1000}
            ]
        )


def test_load_health_diary_using_user_id_and_date(
    user_id: int,
    add_meal_uc: AddingMealToDiary,
    input_dto: AddingMealToDiaryInputdto,
    diary_repo_mock: Mock
) -> None:
    date = datetime.date.today()
    add_meal_uc.execute(input_dto)
    diary_repo_mock.get.assert_called_once_with(user_id, date)


def test_save_health_diary(
        user_id: int,
        add_meal_uc: AddingMealToDiary,
        input_dto: AddingMealToDiaryInputdto,
        diary_repo_mock: Mock,
        ) -> None:

    with patch('health_diary.domain.entities.HealthDiary.add_meals') as mock:
        add_meal_uc.execute(input_dto)
    mock.assert_called_once()
