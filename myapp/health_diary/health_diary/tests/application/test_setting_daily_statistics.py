import pytest
from unittest.mock import Mock
from health_diary.application.use_cases import (
    SettingDailyStatistics,
    SettingDailyStatisticsInputDto,
    )
from .common_fixtures import(
    user_id,
    diary_repo_mock,
    health_diary,
)


@pytest.fixture()
def set_daily_statistic_uc(diary_repo_mock) -> SettingDailyStatistics:
    return SettingDailyStatistics(diary_repo_mock)


@pytest.fixture()
def input_dto(user_id) -> SettingDailyStatisticsInputDto:
    return SettingDailyStatisticsInputDto(user_id)


def test_load_health_diary_using_user_id(
        user_id: int,
        set_daily_statistic_uc: SettingDailyStatistics,
        input_dto: SettingDailyStatisticsInputDto,
        diary_repo_mock: Mock
        ) -> None:
    set_daily_statistic_uc.execute(input_dto)
    diary_repo_mock.get.assert_called_once_with(user_id)


def test_save_health_diary(
        user_id: int,
        set_daily_statistic_uc: SettingDailyStatistics,
        input_dto: SettingDailyStatisticsInputDto,
        diary_repo_mock: Mock
        ) -> None:
    set_daily_statistic_uc.execute(input_dto)
    diary_repo_mock.save.assert_called_once()
