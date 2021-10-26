from .foundation import user
from health_diary_api import models
from health_diary_infrastructure.repositories import DjangoHealthDiaryRepository
from health_diary.domain.entities import HealthDiary, Meal
import datetime
import pytest


@pytest.fixture()
def diary_with_meals(user):
    today = datetime.date.today()
    diary = models.HealthDiary.objects.create(
        user_id=user.id,
        date=today)
    meals = [
        models.Meal.objects.create(diary_id=diary.id, user_id=user.id, date=today,
                                   name='test', calories=1000),
        models.Meal.objects.create(diary_id=diary.id, user_id=user.id, date=today,
                                   name='test2', calories=1000)
        ]
    return diary


@pytest.mark.django_db
def test_getting_diary(user, diary_with_meals) -> None:
    date = datetime.date.today()
    diary = DjangoHealthDiaryRepository.get(user_id=user.id, date=date)
    assert diary.meals[0].name == diary_with_meals.meal_set.all()[0].name


@pytest.mark.django_db
def test_saving_diary(user) -> None:
    meals = [
        Meal.create(user.id, date=datetime.date.today(),
                    name='test1', calories=1000),
        Meal.create(user.id, date=datetime.date.today(),
                    name='test2', calories=1000)
    ]
    diary = HealthDiary(
        user_id=user.id,
        weigth=100,
        rest_hr=54,
        meals=meals
    )
    DjangoHealthDiaryRepository.save(diary)
