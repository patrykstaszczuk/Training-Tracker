from abc import ABC, abstractmethod
from typing import TypedDict
from health_diary.domain.value_objects import (
    Weigth,
    StressScore,
    MoodScore,
    SleepLength,
    RestHr,
)


class HealthDiaryDto(TypedDict):
    user_id: int
    weigth: Weigth = None
    rest_hr: RestHr = None
    morning_stress_score: StressScore = None
    evening_stress_score: StressScore = None
    morning_mood: MoodScore = None
    evening_mood: MoodScore = None
    sleep_length: SleepLength = None


class GettingDailyStatistics(ABC):

    @abstractmethod
    def query(self, user_id: int) -> HealthDiaryDto:
        pass
