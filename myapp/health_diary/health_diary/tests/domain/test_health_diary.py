from health_diary.domain.entities import HealthDiary, Meal
import datetime


def test_adding_meals() -> None:
    diary = HealthDiary(1)
    print(vars(diary))
    meals = [
        Meal(1, datetime.date.today, 'test', 1000),
        Meal(1, datetime.date.today, 'test2', 1000),
        Meal(1, datetime.date.today, 'test3', 1000),
        ]
    diary.add_meals(meals)
    for meal in diary.meals:
        print(meal.name)
    assert len(diary.meals) == 3
