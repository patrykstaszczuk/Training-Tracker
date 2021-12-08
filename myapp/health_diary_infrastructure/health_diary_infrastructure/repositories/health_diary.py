import datetime

import health_diary_api

from health_diary.application.repositories import HealthDiaryRepository
from health_diary.domain.exceptions import (
    DiaryDoesNotExists
)
from health_diary.domain.entities import HealthDiary, Meal


class DjangoHealthDiaryRepository(HealthDiaryRepository):

    def __init__(self):
        self.health_diary_model = health_diary_api.models.HealthDiary
        self.meal_model = health_diary_api.models.Meal

    def get(self, user_id: int, date: datetime = datetime.date.today()) -> HealthDiary:
        if date == datetime.date.today():
            diary, created = self.health_diary_model.objects.get_or_create(
                user_id=user_id, date=date)
        else:
            try:
                diary = self.health_diary_model.objects.get(
                    user_id=user_id, date=date)
            except self.health_diary_model.DoesNotExist:
                raise DiaryDoesNotExists
        return _row_to_entity(diary)

    def save(self, health_diary: HealthDiary):

        diary, created = self.health_diary_model.objects.update_or_create(
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

        for meal in health_diary.meals_to_be_add:
            meal = self.meal_model.objects.create(
                user_id=meal.creator_id,
                date=meal.date,
                name=meal.name,
                calories=meal.calories,
                diary=diary
            )

        if health_diary.meals_to_be_remove:
            self.meal_model.objects.filter(
                user_id=diary.user_id, id__in=health_diary.meals_to_be_remove).delete()


def _row_to_entity(diary) -> HealthDiary:
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
