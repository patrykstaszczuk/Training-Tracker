from users.domain.value_objects import Zones
from users.domain.exceptions import (
    NameTooShort,
    SurnameTooShort,
    IncorrectMainSport,
)


class User:
    def __init__(
        self,
        id: int,
        email: str,
        name: str,
        surname: str,
        password: str,
        main_sport: str,
        weigth: int = None,
        heigth: int = None,
        ftp: int = None,
        max_hr: int = None,
        hr_zones: Zones = None,
        pw_zones: Zones = None,
        lactate_thr: int = None,

    ) -> None:
        self.id = id
        self.email = email
        self.name = name
        self.surname = surname
        self.password = password
        self.main_sport = main_sport
        self.weigth = weigth
        self.heigth = heigth
        self.ftp = ftp
        self.max_hr = max_hr
        self.hr_zones = hr_zones
        self.pw_zones = pw_zones
        self.lactate_thr = lactate_thr

    @staticmethod
    def create(
            email: str,
            name: str,
            surname: str,
            password: str,
            main_sport: str,) -> None:

        if len(name) < 3:
            raise NameTooShort
        if len(surname) < 3:
            raise SurnameTooShort

        if main_sport not in ['cycling', 'triathlon']:
            raise IncorrectMainSport

        user = User(id=id, email=email, name=name, surname=surname,
                    password=password, main_sport=main_sport)
        return user

    def update(self, **attrs):
        for attr in attrs:
            setattr(self, attr, attrs[attr])
