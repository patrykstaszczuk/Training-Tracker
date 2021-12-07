import injector
from health_diary_infrastructure.repositories import DjangoHealthDiaryRepository
from health_diary_infrastructure.queries import (
    DjangoGettingDailyStatistics
)
from health_diary import (
    HealthDiaryRepository,
    GettingDailyStatistics,
)

__all__ = [
    'HealthDiaryInfrastructure'
]


class HealthDiaryInfrastructure(injector.Module):

    @injector.provider
    def health_diary_repo(self) -> HealthDiaryRepository:
        return DjangoHealthDiaryRepository()

    @injector.provider
    def get_heatlh_diary(self) -> GettingDailyStatistics:
        return DjangoGettingDailyStatistics()
