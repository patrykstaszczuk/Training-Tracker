import pytest
import datetime
from unittest.mock import Mock, patch
from planner.domain.entities import (
    AnnualPlan
)
from planner.domain.exceptions import (
    AnnualPlanStartingInThePast,
    InvalidSportDiscipline,
    VolumeExceeded,
)
from planner.application.use_cases import (
    CreatingAnnualPlanInputDto,
    CreatingAnnualPlan
)
from planner.application.repositories import (
    InMemoryAnnualPlanRepository,
)


@pytest.fixture()
def user_id() -> int:
    return 1


@pytest.fixture()
def races_ids() -> list[int]:
    return [1, 2, 3]


@pytest.fixture()
def input_dto(user_id, races_ids) -> CreatingAnnualPlanInputDto:
    return CreatingAnnualPlanInputDto(
        user_id=user_id,
        start_date=datetime.date.today(),
        sport_discipline='cycling',
        races=races_ids,
        volume=600,
        goals='Run 10km under 40 mins'
    )


@pytest.fixture()
def repo() -> InMemoryAnnualPlanRepository:
    return InMemoryAnnualPlanRepository()


@pytest.fixture()
def creating_plan_uc(repo) -> CreatingAnnualPlan:
    return CreatingAnnualPlan(repo)


def custom_input_dto(
    user_id=1,
    start_date=datetime.date.today(),
    sport_discipline='cycling',
    races=[1, 2, 3],
    volume=600,
    goals='Run 10km under 40 mins'
        ) -> CreatingAnnualPlanInputDto:
    return CreatingAnnualPlanInputDto(
        user_id=user_id,
        start_date=start_date,
        sport_discipline=sport_discipline,
        races=races,
        volume=volume,
        goals=goals
    )


def test_call_create_anuall_plan_on_entity(
        input_dto: CreatingAnnualPlanInputDto,
        creating_plan_uc: CreatingAnnualPlan,
        ):
    with patch.object(AnnualPlan, 'create') as call_create_mock:
        creating_plan_uc.execute(input_dto)
    call_create_mock.assert_called_with(**vars(input_dto))


def test_call_save_on_repo(
        input_dto: CreatingAnnualPlanInputDto,
        creating_plan_uc: CreatingAnnualPlan,
        ):
    with patch.object(InMemoryAnnualPlanRepository, 'save') as repo_mock:
        creating_plan_uc.execute(input_dto)
    repo_mock.assert_called_once()


def test_CreatingAnnualPlan_start_in_the_past_raise_exception(
        creating_plan_uc: CreatingAnnualPlan
        ) -> None:
    with pytest.raises(AnnualPlanStartingInThePast):
        creating_plan_uc.execute(custom_input_dto(
            start_date=datetime.date.today() - datetime.timedelta(1)
            ))


def test_CreatingAnnualPlan_wrong_sport_discipline(
        creating_plan_uc: CreatingAnnualPlan
        ) -> None:
    with pytest.raises(InvalidSportDiscipline):
        creating_plan_uc.execute(custom_input_dto(
            sport_discipline='invalid'
            ))


def test_CreatingAnnualPlan_max_volume_exceeded_raise_exception(
        creating_plan_uc: CreatingAnnualPlan
        ) -> None:
    with pytest.raises(VolumeExceeded):
        creating_plan_uc.execute(custom_input_dto(
            volume=365 * 24 + 1
            ))
