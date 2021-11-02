from .foundation import user
from health_diary_api import models
from health_diary_infrastructure.repositories import DjangoHealthDiaryRepository
from health_diary.domain.entities import HealthDiary, Meal
from health_diary.domain.exceptions import DiaryDoesNotExists
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
def test_should_create_diary_for_today_if_not_exists(user) -> None:
    assert DjangoHealthDiaryRepository.get(user_id=user.id)


@pytest.mark.django_db
def test_should_raise_domain_exception_if_diary_for_given_date_not_found(user) -> None:
    with pytest.raises(DiaryDoesNotExists):
        date = datetime.date.today() - datetime.timedelta(1)
        DjangoHealthDiaryRepository.get(
            user_id=user.id, date=date)


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
    )
    diary.add_meals(meals)
    DjangoHealthDiaryRepository.save(diary)

    diary = DjangoHealthDiaryRepository.get(user.id)
    assert len(diary.meals) == 2


@pytest.mark.django_db
def test_remove_meals_from_diary(user) -> None:
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
    )
    diary.add_meals(meals)
    DjangoHealthDiaryRepository.save(diary)

    diary = DjangoHealthDiaryRepository.get(user.id)
    meals_to_be_remove = [diary.meals[0].meal_id]
    diary.remove_meals(meals_to_be_remove)
    DjangoHealthDiaryRepository.save(diary)

    diary = DjangoHealthDiaryRepository.get(user.id)
    assert len(diary.meals) == 1
