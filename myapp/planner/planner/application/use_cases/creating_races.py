from dataclasses import dataclass
import datetime
from planner.application.repositories import RaceRepository
from planner.domain.entities import Race
from planner.domain.exceptions import (
    RaceStartInThePast,
    InvalidSportDiscipline,
    InvalidPriority,
)


@dataclass
class CreatingRaceInputDto:
    user_id: int
    name: str
    start_date: datetime.date
    sport_discipline: str
    priority: str


class CreatingRace:
    def __init__(
        self,
        repo: RaceRepository
    ) -> None:
        self.repo = repo

    def execute(self, input_dto: CreatingRaceInputDto) -> None:

        if input_dto.start_date < datetime.date.today():
            raise RaceStartInThePast()
        if input_dto.sport_discipline not in ['cycling', 'running', 'triathlon']:
            raise InvalidSportDiscipline()
        if input_dto.priority not in ['A', 'B', 'C']:
            raise InvalidPriority()

        race = Race.create(
            user_id=input_dto.user_id,
            name=input_dto.name,
            start_date=input_dto.start_date,
            sport_discipline=input_dto.sport_discipline,
            priority=input_dto.priority
        )
        self.repo.save(race)
