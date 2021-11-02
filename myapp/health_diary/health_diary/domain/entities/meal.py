import datetime
from health_diary.domain.exceptions import (
    MealNameTooLong,
)


class Meal:
    def __init__(
        self,
        creator_id: int,
        date: datetime.date,
        name: str,
        calories: int,
        meal_id: int = None,
    ) -> None:
        self.creator_id = creator_id
        self.date = date
        self.name = name
        self.calories = calories
        self.meal_id = meal_id

    @staticmethod
    def create(creator_id: int, date: datetime.date, name: str, calories: int):
        return Meal(
            creator_id=creator_id,
            date=date,
            name=name,
            calories=calories
        )
