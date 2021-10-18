from dataclasses import dataclass
from health_diary.application.repositories import HealthDiaryRepository


@dataclass(frozen=True)
class SettingDailyStatisticsInputDto:
    user_id: int
    weigth: int = None
    rest_hr: int = None
    morning_stress_score: int = None
    evening_stress_score: int = None
    morning_mood: int = None
    evening_mood: int = None
    sleep_length: int = None


class SettingDailyStatistics:
    def __init__(
            self,
            repo: HealthDiaryRepository
            ) -> None:
        self.repo = repo

    def execute(self, input_dto: SettingDailyStatisticsInputDto) -> None:
        diary = self.repo.get(input_dto.user_id)
        diary.set_attrs(
            weigth=input_dto.weigth,
            rest_hr=input_dto.rest_hr,
            morning_stress_score=input_dto.morning_stress_score,
            evening_stress_score=input_dto.evening_stress_score,
            moring_mood=input_dto.morning_mood,
            evening_mood=input_dto.evening_mood,
            sleep_length=input_dto.sleep_length,
        )
        self.repo.save(diary)
