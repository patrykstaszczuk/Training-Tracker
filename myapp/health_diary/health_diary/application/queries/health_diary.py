from abc import ABC, abstractmethod
from typing import TypedDict, List
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
    date: datetime.datetime
    weigth: Weigth
    rest_hr: RestHr
    morning_stress_score: StressScore
    evening_stress_score: StressScore
    morning_mood: MoodScore
    evening_mood: MoodScore
    sleep_length: SleepLength


class ListOfDiariesDto(TypedDict):
    id = int
    date = datetime.datetime
    url = None

    diaries: list[dict[str, id | date | url]]


class SpecificStatisticHistoryDto(TypedDict):
    values: List[int | float | datetime.datetime]


class GettingDailyStatistics(ABC):
    """ abc class for retreiving statistics for given day"""

    @abstractmethod
    def query(self, user_id: int, date: datetime) -> HealthDiaryDto:
        pass


class GettingListOfDiaries(ABC):
    """ abc class for retrieving list of diaries """

    @abstractmethod
    def query(self, user_id: int) -> ListOfDiariesDto:
        pass


class GettingSpecificStatistic(ABC):
    """ abc class for retrieving given number of specific statistic based
     on the name """

    @abstractmethod
    def query(self, user_id: int, statistic: str, number: int) -> SpecificStatisticHistoryDto:
        pass
