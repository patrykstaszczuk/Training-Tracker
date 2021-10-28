from abc import ABC, abstractmethod
from planner.domain.entities import AnnualPlan
import copy


class AnnualPlanRepository(ABC):

    @abstractmethod
    def get(user_id: int) -> AnnualPlan:
        pass

    @abstractmethod
    def save(annual_plan: AnnualPlan) -> None:
        pass


class InMemoryAnnualPlanRepository(AnnualPlanRepository):
    """ in memory db implementation for testing purpose """

    def __init__(self) -> None:
        self._storage: dict[int, AnnualPlan] = {}

    def get(self, user_id: int) -> AnnualPlan:
        return copy.deepcopy(self._storage[user_id])

    def save(self, annual_plan: AnnualPlan) -> None:
        self._storage[annual_plan.user_id] = copy.deepcopy(annual_plan)
