from health_diary.application.repositories import HealthDiaryRepository
from health_diary.domain.exceptions import (
    DiaryDoesNotExists
)
from health_diary.domain.entities import HealthDiary, Meal
from health_diary_api import models
import datetime


class DjangoHealthDiaryRepository(HealthDiaryRepository):

    def get(user_id: int, date: datetime = datetime.date.today()) -> HealthDiary:
        if date == datetime.date.today():
            diary, created = models.HealthDiary.objects.get_or_create(
                user_id=user_id, date=date)
        else:
            try:
                diary = models.HealthDiary.objects.get(
                    user_id=user_id, date=date)
            except models.HealthDiary.DoesNotExist:
                raise DiaryDoesNotExists
        return _row_to_entity(diary)

    def save(health_diary: HealthDiary):

        diary, created = models.HealthDiary.objects.update_or_create(
            user_id=health_diary.user_id,
            date=datetime.date.today(),
            defaults={
                'user_id': health_diary.user_id,
                'rest_hr': health_diary.rest_hr,
                'morning_sress_score': health_diary.morning_sress_score,
                'evening_stress_score': health_diary.evening_stress_score,
                'morning_mood': health_diary.morning_mood,
                'evening_mood': health_diary.evening_mood,
                'sleep_length': health_diary.sleep_length,
            }
        )
        for meal in health_diary.meals:
            meal = models.Meal.objects.create(
                user_id=meal.creator_id,
                date=meal.date,
                name=meal.name,
                calories=meal.calories,
                diary=diary
            )


def _row_to_entity(diary: models.HealthDiary) -> HealthDiary:
    meals = []
    for meal in diary.meal_set.all():
        meals.append(
            Meal(
                creator_id=meal.user_id,
                date=meal.date,
                name=meal.name,
                calories=meal.calories,
                meal_id=meal.id
            )
        )
    return HealthDiary(
        user_id=diary.user_id,
        weigth=diary.weigth,
        rest_hr=diary.rest_hr,
        morning_sress_score=diary.morning_sress_score,
        evening_stress_score=diary.evening_stress_score,
        morning_mood=diary.morning_mood,
        evening_mood=diary.evening_mood,
        sleep_length=diary.sleep_length,
        meals=meals
    )
