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
    ) -> None:
        self.creator_id = creator_id
        self.date = date
        self.name = name
        self.calories = calories

        if len(name) > 20:
            raise MealNameTooLong()

    @staticmethod
    def create(creator_id: int, date: datetime.date, name: str, calories: int):
        return Meal(
            creator_id=creator_id,
            date=date,
            name=name,
            calories=calories
        )
