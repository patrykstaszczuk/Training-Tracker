from abc import ABC, abstractmethod
from typing import TypedDict
from health_diary.domain.value_objects import (
    Weigth,
    StressScore,
    MoodScore,
    SleepLength,
    RestHr,
)
import datetime


class HealthDiaryDto(TypedDict):
    user_id: int
    date: str
    weigth: Weigth
    rest_hr: RestHr
    morning_stress_score: StressScore
    evening_stress_score: StressScore
    morning_mood: MoodScore
    evening_mood: MoodScore
    sleep_length: SleepLength


class GettingDailyStatistics(ABC):
    """ abc class for retreiving statistics for given day"""

    @abstractmethod
    def query(self, user_id: int, date: datetime) -> HealthDiaryDto:
        pass


class GettingSpecificStatistic(ABC):
    """ abc class for retrieving specific statiscit based on the name """
    pass
