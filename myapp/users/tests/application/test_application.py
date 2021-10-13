from django.test import TestCase
from users.application.use_cases import (
    CreateUser,
    CreateUserInputDto,
    SetTraningSpecificInformation,
    SetTraningSpecificInformationDto,
)
from users.application.repositories import (
    UsersRepository,
    InMemoryUserRepository,
    )
from users.domain.exceptions import (
    NameTooShort,
    SurnameTooShort,
    IncorrectMainSport,
)
from users import User


def create_user(repo: UsersRepository) -> CreateUser:
    return CreateUser(repo)


def set_user_training_attributes(repo: UsersRepository) -> SetTraningSpecificInformation:
    return SetTraningSpecificInformation(repo)


class UseCases(TestCase):

    def setUp(self) -> None:
        self.repo = InMemoryUserRepository()
        user = User(id=1, email='test@gmail.com', name='test', surname='test2334',
                    password='testpass', main_sport='cycling')
        self.repo.save(user)

    def test_create_user_succeed(self) -> None:

        input_dto = CreateUserInputDto(
            email='test2@gmail.com',
            name='test',
            surname='test',
            password='testpass',
            main_sport='cycling',

        )
        create_user(self.repo).execute(input_dto)

    def test_create_user_name_and_surname_too_short(self) -> None:
        input_dto = CreateUserInputDto(
            email='test2@gmail.com',
            name='t',
            surname='t',
            password='testpass',
            main_sport='cycling',

        )
        with self.assertRaises((NameTooShort, SurnameTooShort)):
            create_user(self.repo).execute(input_dto)

    def test_create_user_with_invalid_main_sport(self) -> None:
        input_dto = CreateUserInputDto(
            email='test2@gmail.com',
            name='test',
            surname='test222',
            password='testpass',
            main_sport='other then cycling or triathlon',

        )
        with self.assertRaises(IncorrectMainSport):
            create_user(self.repo).execute(input_dto)

    def test_set_extra_user_information_succeed(self) -> None:
        user = self.repo.get(user_id=1)
        input_dto = SetTraningSpecificInformationDto(
            id=user.id,
            weigth=75,
            heigth=188,
            ftp=300,
            max_hr=195,
            lactate_thr=172
        )
        set_user_training_attributes(self.repo).execute(input_dto)
        user = self.repo.get(user_id=1)

        assert user.weigth == input_dto.weigth
        assert user.heigth == input_dto.heigth
        assert user.ftp == input_dto.ftp
        assert user.max_hr == input_dto.max_hr
        assert user.lactate_thr == input_dto.lactate_thr

    # def test_setting_training_zones_success(self) -> None:
    #     user = self.repo.get(user_id=1)
    #
    #     input_dto = SetTrainingZones(
    #         id=user.id,
    #
    #
    #     )
