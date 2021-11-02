from dataclasses import dataclass
import datetime
from planner.domain.entities import AnnualPlan, Race
from planner.domain.exceptions import (
    AnnualPlanStartingInThePast,
    InvalidSportDiscipline,
    VolumeExceeded
)
from planner.application.repositories import AnnualPlanRepository


@dataclass(frozen=True)
class CreatingAnnualPlanInputDto:
    user_id: int
    start_date: datetime.date
    sport_discipline: str
    volume: int
    races: list[Race, ] = None
    goals: str = None


class CreatingAnnualPlan:
    def __init__(
        self,
        repo: AnnualPlanRepository
    ) -> None:
        self.repo = repo

    def execute(self, input_dto: CreatingAnnualPlanInputDto) -> None:
        if input_dto.start_date < datetime.date.today():
            raise AnnualPlanStartingInThePast(
                'Annual plan cannot start in the past')
        if input_dto.sport_discipline not in ['cycling', 'running', 'triathlon']:
            raise InvalidSportDiscipline(
                'Invalid sport discipline, choose from "cycling, running, triathlon"')
        if input_dto.volume > 365 * 24:
            raise VolumeExceeded('Volume cannot be greater then ')
        annual_plan = AnnualPlan.create(**vars(input_dto))
        self.repo.save(annual_plan)
