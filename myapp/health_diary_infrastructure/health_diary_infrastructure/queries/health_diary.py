from health_diary.application.queries import (
    GettingDailyStatistics,
    GettingSpecificStatistic,
    HealthDiaryDto,
    SpecificStatisticHistoryDto,
)
import health_diary_api
from typing import List
import datetime


class DjangoGettingDailyStatistics(GettingDailyStatistics):

    def __init__(self):
        self.health_diary_model = health_diary_api.models.HealthDiary

    def query(
            self,
            user_id: int,
            date: datetime = datetime.date.today()
            ) -> HealthDiaryDto:
        diary = self.health_diary_model.objects.get(user_id=user_id, date=date)
        return self._row_to_typed_dict(diary)

    def _row_to_typed_dict(self, diary: object) -> HealthDiaryDto:
        dict = HealthDiaryDto(
            user_id=diary.user_id,
            date=diary.date,
            weigth=diary.weigth,
            rest_hr=diary.rest_hr,
            morning_sress_score=diary.morning_sress_score,
            evening_stress_score=diary.evening_stress_score,
            morning_mood=diary.morning_mood,
            evening_mood=diary.evening_mood,
            sleep_length=diary.sleep_length,
        )
        return dict


class DjangoGettingSpecificStatisticHistory(GettingSpecificStatistic):

    def __init__(self):
        self.health_diary_model = health_diary_api.models.HealthDiary

    def query(self, user_id: int, statistic: str, number: int = 7) -> SpecificStatisticHistoryDto:
        list_of_values = self.health_diary_model.objects.filter(
            user_id=user_id,
            ).values_list(statistic, flat=True)[:number]
        return self._row_to_typed_dict(list_of_values)

    def _row_to_typed_dict(self, values) -> SpecificStatisticHistoryDto:
        dict = SpecificStatisticHistoryDto(
            values=list(values)
            )
        return dict
