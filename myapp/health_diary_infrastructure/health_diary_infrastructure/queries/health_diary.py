from health_diary.application.queries import (
    GettingDailyStatistics,
    HealthDiaryDto,
)
from health_diary_api import models


class DjangoGettingDailyStatistics(GettingDailyStatistics):

    def query(self, user_id: int) -> HealthDiaryDto:
        diary = models.HealthDiary.objects.get(user_id=user_id)
        return _row_to_typed_dict(diary)


def _row_to_typed_dict(diary: object) -> HealthDiaryDto:
    dict = HealthDiaryDto(
        user_id=diary.user_id,
        weigth=diary.weigth,
        rest_hr=diary.rest_hr,
        morning_sress_score=diary.morning_sress_score,
        evening_stress_score=diary.evening_stress_score,
        moring_mood=diary.moring_mood,
        evening_mood=diary.evening_mood,
        sleep_length=diary.sleep_length,
    )
    return dict
