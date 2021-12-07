import injector

from health_diary.application.queries import (
    GettingDailyStatistics,
    GettingListOfDiaries,
)
from health_diary.application.repositories import HealthDiaryRepository


__all__ = [
    #queries
    "GettingDailyStatistics",
    "GettingListOfDiaries",
    'HealthDiaryRepository'
]
