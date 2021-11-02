from dataclasses import dataclass
from health_diary.application.repositories import HealthDiaryRepository
import datetime


@dataclass
class DeletingMealFromDiaryInputDto:
    user_id: int
    date: datetime.date
    meal_ids: list[int]


class DeletingMealFromDiary:
    def __init__(
        self,
        repo: HealthDiaryRepository
    ) -> None:
        self.repo = repo

    def execute(self, input_dto: DeletingMealFromDiaryInputDto) -> None:
        diary = self.repo.get(input_dto.user_id, input_dto.date)
        diary.remove_meals(input_dto.meal_ids)
        self.repo.save(diary)
