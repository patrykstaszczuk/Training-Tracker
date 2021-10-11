from dataclasses import dataclass
from users.domain.value_objects import (
    UserEmail,
    UserName,
    UserSurname,
    UserMainSport,
    UserHrZones,
    UserPwZones,
    UserMaxHr,
    )


@dataclass(frozen=True)
class CreateUserInputDto:
    email: UserEmail
    name: UserName
    surname: UserSurname
    main_sport: UserMainSport
    weigth: int
    heigth: int
    ftp: int = None
    hr_zones: UserHrZones = None
    pw_zones: UserPwZones = None
    max_hr: UserMaxHr = None


class CreateUser:

    def execute(self, input_dto: CreateUserInputDto) -> None:
        pass
