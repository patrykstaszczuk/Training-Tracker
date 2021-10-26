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


def test_create_meal_name_too_long() -> None:
    with pytest.raises(MealNameTooLong):
        Meal(
            creator_id=1,
            date=datetime.date.today(),
            name='mealmusthaveatmost20characters',
            calories=1000,
        )
