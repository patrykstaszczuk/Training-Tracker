from health_diary.application.repositories import HealthDiaryRepository
from health_diary.domain.entities import HealthDiary


class DjangoHealthDiaryRepository(HealthDiaryRepository):

    def get(user_id: int) -> HealthDiary:
        pass

    def save():
        pass
