from django.test import TestCase
from unittest.mock import Mock
from profile.application.use_cases import (
    SetTraningSpecificInformation,
    SetTraningSpecificInformationDto,
    SetHrTrainingZones,
    SetHrTrainingZonesDto
)
from profile.application.repositories import (
    ProfileRepository,
    InMemoryProfileRepository,
    )
from profile.domain.exceptions import (
    IncorrectMainSport,
)
from profile import (
    UserProfile,
    Zones,
    ZonePercent,
    SetHrTrainingZonesBoundary,
    SetHrTrainingZonesOutputDto
)


def set_user_training_attributes(repo: ProfileRepository) -> SetTraningSpecificInformation:
    return SetTraningSpecificInformation(repo)


def set_hr_zones(
        output_boundary: SetHrTrainingZonesBoundary,
        repo: ProfileRepository
        ) -> SetHrTrainingZones:
    return SetHrTrainingZones(output_boundary, repo)


class UseCases(TestCase):

    def setUp(self) -> None:
        self.repo = InMemoryProfileRepository()
        profile = UserProfile(user_id=1, main_sport='cycling', lactate_thr=172)
        self.repo.save(profile)

    # def test_create_user_succeed(self) -> None:
    #
    #     input_dto = CreateUserInputDto(
    #         email='test2@gmail.com',
    #         name='test',
    #         surname='test',
    #         password='testpass',
    #         main_sport='cycling',
    #
    #     )
    #     create_user(self.repo).execute(input_dto)
    #
    # def test_create_user_name_and_surname_too_short(self) -> None:
    #     input_dto = CreateUserInputDto(
    #         email='test2@gmail.com',
    #         name='t',
    #         surname='t',
    #         password='testpass',
    #         main_sport='cycling',
    #
    #     )
    #     with self.assertRaises((NameTooShort, SurnameTooShort)):
    #         create_user(self.repo).execute(input_dto)
    #
    # def test_create_user_with_invalid_main_sport(self) -> None:
    #     input_dto = CreateUserInputDto(
    #         email='test2@gmail.com',
    #         name='test',
    #         surname='test222',
    #         password='testpass',
    #         main_sport='other then cycling or triathlon',
    #
    #     )
    #     with self.assertRaises(IncorrectMainSport):
    #         create_user(self.repo).execute(input_dto)

    def test_set_extra_user_information_succeed(self) -> None:
        profile = self.repo.get(user_id=1)
        input_dto = SetTraningSpecificInformationDto(
            user_id=profile.user_id,
            weigth=75,
            heigth=188,
            ftp=300,
            max_hr=195,
            lactate_thr=172
        )
        set_user_training_attributes(self.repo).execute(input_dto)
        profile = self.repo.get(user_id=1)

        assert profile.weigth == input_dto.weigth
        assert profile.heigth == input_dto.heigth
        assert profile.ftp == input_dto.ftp
        assert profile.max_hr == input_dto.max_hr
        assert profile.lactate_thr == input_dto.lactate_thr

    def test_setting_training_zones_success_with_proper_output(self) -> None:
        profile = self.repo.get(user_id=1)
        profile.max_hr = 195
        self.repo.save(profile)

        zones_list = [
            ZonePercent(50),
            ZonePercent(80),
            ZonePercent(85),
            ZonePercent(90),
            ZonePercent(95),
        ]
        input_dto = SetHrTrainingZonesDto(
            user_id=profile.user_id,
            zones=Zones(*zones_list)
        )
        output_boundary_mock = Mock(spec_set=SetHrTrainingZonesBoundary)
        set_hr_zones(output_boundary_mock, self.repo).execute(input_dto)
        profile = self.repo.get(user_id=1)
        excepted_zones = profile.calculate_hr_zones_based_on_lactate_threshold()
        expected_output_dto = SetHrTrainingZonesOutputDto(
            zones=excepted_zones
        )
        output_boundary_mock.present.assert_called_once_with(
            expected_output_dto)
