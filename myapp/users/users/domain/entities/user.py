from users.domain.value_objects import Zones
from users.domain.exceptions import (
    NameTooShort,
    SurnameTooShort,
    IncorrectMainSport,
    LactateThresholdNotSet,
    MaxHrNotSet,
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

    def set_hr_zones(self, zones: Zones) -> None:
        """ set heart rate zones """
        if self.lactate_thr is None:
            raise LactateThresholdNotSet
        if self.max_hr is None:
            raise MaxHrNotSet
        setattr(self, 'hr_zones', zones)

    def calculate_hr_zones_based_on_lactate_threshold(self):
        zones = [(zone, int(value)) for zone in vars(self.hr_zones).values()
                 for value in [self.lactate_thr * zone/100]]
        fifth_zone = (100, self.lactate_thr)
        max_hr_percent = int(self.max_hr/self.lactate_thr * 100)
        sixth_zone = (max_hr_percent, self.max_hr)
        zones.append(fifth_zone)
        zones.append(sixth_zone)
        return zones
