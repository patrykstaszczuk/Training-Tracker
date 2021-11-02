import datetime
from planner.domain.entities.race import Race


class AnnualPlan:
    def __init__(
        self,
        user_id: int,
        start_date: datetime.date,
        sport_discipline: str,
        volume: int,
        races: list[Race, ] = None,
        goals: str = None,

    ) -> None:
        self.user_id = user_id
        self.start_date = start_date
        self.sport_discipline = sport_discipline
        self.races = races
        self.volume = volume
        self.goals = goals

    @property
    def end_date(self) -> datetime.date:
        return self.start_date + datetime.timedelta(365)

    @staticmethod
    def create(
        user_id: int,
        start_date: datetime.date,
        sport_discipline: str,
        races: list[Race],
        volume: int,
        goals: str
    ) -> 'AnnualPlan':
        return AnnualPlan(
            user_id=user_id,
            start_date=start_date,
            sport_discipline=sport_discipline,
            races=races,
            volume=volume,
            goals=goals
        )
