import pytest
import datetime
from unittest.mock import Mock, patch
from planner.application.use_cases import(
    CreatingRaceInputDto,
    CreatingRace
)
from planner.application.repositories import InMemoryRaceRepository
from planner.domain.entities import Race
from planner.domain.exceptions import(
    RaceStartInThePast,
    InvalidSportDiscipline,
    InvalidPriority,
)


@pytest.fixture()
def repo() -> InMemoryRaceRepository:
    return InMemoryRaceRepository()


@pytest.fixture()
def input_dto() -> CreatingRaceInputDto:
    return CreatingRaceInputDto(
        user_id=1,
        name='Race 1',
        start_date=datetime.date.today(),
        sport_discipline='cycling',
        priority='A'
    )


@pytest.fixture()
def creating_race_uc(repo) -> CreatingRace:
    return CreatingRace(repo)


def custom_input_dto(
        user_id=1,
        name='Race 1',
        start_date=datetime.date.today(),
        sport_discipline='cycling',
        priority='A'
        ) -> CreatingRaceInputDto:
    return CreatingRaceInputDto(
        user_id=user_id,
        name=name,
        start_date=start_date,
        sport_discipline=sport_discipline,
        priority=priority,
    )


def test_call_create_on_race_entity(
        input_dto: CreatingRaceInputDto,
        creating_race_uc: CreatingRace
        ) -> None:
    with patch.object(Race, 'create') as call_create_mock:
        creating_race_uc.execute(input_dto)
    call_create_mock.assert_called_with(**vars(input_dto))


def test_call_save_on_repo(
        input_dto: CreatingRaceInputDto,
        creating_race_uc: CreatingRace,
        ):
    with patch.object(InMemoryRaceRepository, 'save') as repo_mock:
        creating_race_uc.execute(input_dto)
    repo_mock.assert_called_once()


def test_CreatingRace_with_date_in_the_past_raise_exception(
        creating_race_uc: CreatingRace
        ) -> None:
    with pytest.raises(RaceStartInThePast):
        creating_race_uc.execute(custom_input_dto(
            start_date=datetime.date.today() - datetime.timedelta(1)
        ))


def test_CreatingRace_with_invalid_sport_discipline_raise_exception(
        creating_race_uc: CreatingRace
        ) -> None:
    with pytest.raises(InvalidSportDiscipline):
        creating_race_uc.execute(custom_input_dto(
            sport_discipline='invalid'
        ))


def test_CreatingRace_with_invlid_priority_raise_exceptipn(
        creating_race_uc: CreatingRace
        ) -> None:
    with pytest.raises(InvalidPriority):
        creating_race_uc.execute(custom_input_dto(
            priority='invalid'
        ))
