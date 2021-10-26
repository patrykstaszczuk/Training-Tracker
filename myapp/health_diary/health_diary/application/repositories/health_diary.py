from abc import ABC, abstractmethod
from health_diary.domain.entities import HealthDiary
import copy
from typing import Dict
import datetime


class HealthDiaryRepository(ABC):

    @abstractmethod
    def get(self, user_id: int, date: datetime) -> HealthDiary:
        pass

    @abstractmethod
    def save(self, health_diary: HealthDiary) -> None:
        pass


class InMemoryHealthDiaryRepository(HealthDiaryRepository):
    """ in memory db implementation for testing purpose """

    def __init__(self) -> None:
        self._storage: Dict[int, HealthDiary] = {}

    def get(self, user_id: int) -> HealthDiary:
        return copy.deepcopy(self._storage[user_id])

    def save(self, profile: HealthDiary) -> None:
        self._storage[profile.user_id] = copy.deepcopy(profile)
