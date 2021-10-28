import datetime
import pytest
from health_diary.domain.entities import Meal
from health_diary.domain.exceptions import(
    MealNameTooLong,
)


def test_create_meal_success() -> None:
    Meal(
        creator_id=1,
        date=datetime.date.today(),
        name='test dish',
        calories=1000,
    )
