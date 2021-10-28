import datetime


class Race:
    def __init__(
        self,
        user_id: int,
        name: str,
        start_date: datetime.date,
        sport_discipline: str,
        priority: str
    ) -> None:
        self.user_id = user_id
        self.name = name
        self.start_date = start_date
        self.sport_discipline = sport_discipline
        self.priority = priority

    @staticmethod
    def create(
        user_id: int,
        name: str,
        start_date: datetime.date,
        sport_discipline: str,
        priority: str
    ) -> 'Race':
        return Race(
            user_id=user_id,
            name=name,
            start_date=start_date,
            sport_discipline=sport_discipline,
            priority=priority
        )
