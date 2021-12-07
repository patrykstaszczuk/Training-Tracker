import injector

from health_diary.application.queries import (
    GettingDailyStatistics,
)
from health_diary.application.repositories import HealthDiaryRepository


__all__ = [
    #queries
    "GettingDailyStatistics",
    'HealthDiaryRepository'
]
