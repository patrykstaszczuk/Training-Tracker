from abc import ABC, abstractmethod
from planner.domain.entities import Race
import copy


class RaceRepository(ABC):

    @abstractmethod
    def get(user_id: int) -> Race:
        pass

    @abstractmethod
    def save(annual_plan: Race) -> None:
        pass


class InMemoryRaceRepository(RaceRepository):
    """ in memory db implementation for testing purpose """

    def __init__(self) -> None:
        self._storage: dict[int, Race] = {}

    def get(self, user_id: int) -> Race:
        return copy.deepcopy(self._storage[user_id])

    def save(self, race: Race) -> None:
        self._storage[race.user_id] = copy.deepcopy(race)
