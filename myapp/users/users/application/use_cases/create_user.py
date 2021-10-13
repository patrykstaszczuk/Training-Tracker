from dataclasses import dataclass
from users.domain.value_objects import (
    UserId,
    )
from users.application.repositories import UsersRepository
from users.domain.entities import User
from abc import ABC, abstractmethod


@dataclass(frozen=True)
class CreateUserInputDto:
    email: str
    name: str
    surname: str
    password: str
    main_sport: str


class CreateUser:

    def __init__(
        self,
        users_repo: UsersRepository,
    ) -> None:
        self._users_repository = users_repo

    def execute(self, input_dto: CreateUserInputDto) -> None:
        user = User.create(
            email=input_dto.email,
            name=input_dto.name,
            surname=input_dto.surname,
            password=input_dto.password,
            main_sport=input_dto.main_sport,
            )
        self._users_repository.save(user)
