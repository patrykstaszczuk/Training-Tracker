from health_diary.domain.entities import HealthDiary, Meal
import datetime


def test_adding_meals() -> None:
    diary = HealthDiary(1)
    meals = [
        Meal(1, datetime.date.today, 'test', 1000),
        Meal(1, datetime.date.today, 'test2', 1000),
        Meal(1, datetime.date.today, 'test3', 1000),
        ]
    diary.add_meals(meals)
    assert len(diary._meals_to_be_add) == 3
