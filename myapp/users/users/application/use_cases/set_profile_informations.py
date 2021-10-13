from dataclasses import dataclass
from users.domain.value_objects import (
    UserId,
    Zones
    )
from users.application.repositories import UsersRepository
from users.domain.entities import User
from abc import ABC, abstractmethod


@dataclass(frozen=True)
class SetTraningSpecificInformationDto:
    id: UserId
    weigth: int = None
    heigth: int = None
    ftp: int = None
    max_hr: int = None
    hr_zones: Zones = None
    pw_zones: Zones = None
    lactate_thr: int = None


class SetTraningSpecificInformation:
    """ setting additional information about user profile """

    def __init__(
        self,
        users_repo: UsersRepository,
    ) -> None:
        self.users_repo = users_repo

    def execute(self, input_dto: SetTraningSpecificInformationDto) -> None:
        user = self.users_repo.get(input_dto.id)
        user.update(
            weigth=input_dto.weigth,
            heigth=input_dto.heigth,
            ftp=input_dto.ftp,
            max_hr=input_dto.max_hr,
            hr_zones=input_dto.hr_zones,
            pw_zones=input_dto.pw_zones,
            lactate_thr=input_dto.lactate_thr
        )
        self.users_repo.save(user)
