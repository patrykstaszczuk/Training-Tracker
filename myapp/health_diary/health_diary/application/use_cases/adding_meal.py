from health_diary.application.repositories import HealthDiaryRepository
from health_diary.domain.entities import Meal
from health_diary.domain.exceptions import (
    MealNameTooLong,
)
import datetime
from dataclasses import dataclass

Meals = list[dict[str, int | str]]


@dataclass(frozen=True)
class AddingMealToDiaryInputdto:
    creator_id: int
    date: datetime.date
    meals: Meals


class AddingMealToDiary:
    def __init__(
        self,
        repo: HealthDiaryRepository
    ) -> None:
        self.repo = repo

    def execute(self, input_dto: AddingMealToDiaryInputdto) -> None:
        diary = self.repo.get(input_dto.creator_id, input_dto.date)
        meals = []
        for meal in input_dto.meals:
            if len(meal['name']) > 20:
                raise MealNameTooLong()
            meals.append(
                Meal.create(
                    creator_id=input_dto.creator_id,
                    date=input_dto.date,
                    name=meal['name'],
                    calories=meal['calories'],
                ))
        diary.add_meals(meals)
        self.repo.save(diary)
