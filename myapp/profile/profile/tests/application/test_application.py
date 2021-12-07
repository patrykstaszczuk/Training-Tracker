import pytest
from unittest.mock import Mock
from profile.application.use_cases import (
    CreateUserProfile,
    CreateUserProfileDto,
    SetTrainingSpecificInformation,
    SetTrainingSpecificInformationDto,
    SetHrTrainingZones,
    SetTrainingZonesDto,
    SetPowerTrainingZones,
)
from profile.application.repositories import (
    ProfileRepository,
    InMemoryProfileRepository,
    )

from profile import (
    PowerZones,
    HrZones,
    UserProfile,
    ZonePercent,
    SetTrainingZonesBoundary,
    SetTrainingZonesOutputDto,
)
from profile.domain.value_objects import (
    MainSport,
    Height,
    Ftp,
    MaxHr,
    LactateThr,
    )
from profile.domain.exceptions import (
    ProfileAlreadyCreated,
)


def set_user_training_attributes(repo: ProfileRepository) -> SetTrainingSpecificInformation:
    return SetTrainingSpecificInformation(repo)


def create_profile(repo: ProfileRepository) -> CreateUserProfile:
    return CreateUserProfile(repo)


def set_hr_zones(
        repo: ProfileRepository
        ) -> SetHrTrainingZones:
    return SetHrTrainingZones(repo)


def set_pw_zones(
        repo: ProfileRepository
        ) -> SetPowerTrainingZones:
    return SetPowerTrainingZones(repo)


@pytest.fixture()
def profile() -> UserProfile:
    return UserProfile(user_id=1, main_sport='cycling')


@pytest.fixture()
def repo(profile: UserProfile) -> ProfileRepository:
    repo = InMemoryProfileRepository()
    repo.save(profile)
    return repo


@pytest.fixture()
def profile_repo_mock(profile: UserProfile) -> Mock:
    return Mock(
        spec_set=ProfileRepository,
        save=Mock(side_effect=ProfileAlreadyCreated()))


def test_create_basic_user_profile_success(repo: ProfileRepository) -> None:

    input_dto = CreateUserProfileDto(
        user_id=1,
        main_sport=MainSport('cycling'),
        height=Height(188),
    )
    create_profile(repo).execute(input_dto)
    assert repo.get(1).height == input_dto.height.value


def test_profile_already_created(profile_repo_mock) -> None:
    with pytest.raises(ProfileAlreadyCreated):
        input_dto = CreateUserProfileDto(
            user_id=1,
            main_sport=MainSport('cycling'),
            height=Height(188),
        )
        create_profile(profile_repo_mock).execute(input_dto)


def test_set_extra_user_information_succeed(repo: ProfileRepository) -> None:
    profile = repo.get(user_id=1)
    input_dto = SetTrainingSpecificInformationDto(
        user_id=profile.user_id,
        heigth=188,
        ftp=300,
        max_hr=195,
        lactate_thr=172
    )
    set_user_training_attributes(repo).execute(input_dto)
    profile = repo.get(user_id=1)

    assert profile.heigth == input_dto.heigth
    assert profile.ftp == input_dto.ftp
    assert profile.max_hr == input_dto.max_hr
    assert profile.lactate_thr == input_dto.lactate_thr


def test_setting_hr_zones_success_with_proper_output(repo: ProfileRepository) -> None:
    profile = repo.get(user_id=1)
    profile.lactate_thr = 172
    profile.max_hr = 195
    repo.save(profile)

    zones_list = [
        ZonePercent(50),
        ZonePercent(80),
        ZonePercent(85),
        ZonePercent(90),
        ZonePercent(95),
    ]
    input_dto = SetTrainingZonesDto(
        user_id=profile.user_id,
        zones=HrZones(*zones_list)
    )
    set_hr_zones(repo).execute(input_dto)


def test_setting_power_zones_success(repo: ProfileRepository) -> None:
    profile = repo.get(user_id=1)
    profile.ftp = 300
    repo.save(profile)

    zones_list = [
        ZonePercent(50),
        ZonePercent(80),
        ZonePercent(85),
        ZonePercent(90),
        ZonePercent(95),
        ZonePercent(104)
    ]
    input_dto = SetTrainingZonesDto(
        user_id=profile.user_id,
        zones=PowerZones(*zones_list)
    )
    set_pw_zones(repo).execute(input_dto)
    profile = repo.get(user_id=1)
