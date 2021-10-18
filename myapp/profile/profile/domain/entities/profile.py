from profile.domain.value_objects import (
    Zones,
    UserId,
    MainSport,
    Weigth,
    Heigth,
    Ftp,
    MaxHr,
    LactateThr,
    )
from profile.domain.exceptions import (
    IncorrectMainSport,
    LactateThresholdNotSet,
    FtpNotSet,
    MaxHrNotSet,
    MissingUserId,
)
from typing import Dict


class UserProfile:
    def __init__(
        self,
        user_id: int,
        main_sport: MainSport,
        heigth: Heigth = None,
        ftp: Ftp = None,
        max_hr: MaxHr = None,
        hr_zones: Zones = None,
        pw_zones: Zones = None,
        lactate_thr: LactateThr = None,

    ) -> None:
        self.user_id = user_id
        self.main_sport = main_sport
        self.heigth = heigth
        self.ftp = ftp
        self.max_hr = max_hr
        self.hr_zones = hr_zones
        self.pw_zones = pw_zones
        self.lactate_thr = lactate_thr

    @staticmethod
    def create(user_id: UserId, attrs) -> 'UserProfile':
        profile = UserProfile(
            user_id=user_id,
            **attrs
        )
        return profile

    def update(self, **attrs: Dict) -> None:
        for attr in attrs:
            setattr(self, attr, attrs[attr])

    def set_hr_zones(self, zones: Zones) -> None:
        """ set heart rate zones """
        if self.lactate_thr is None:
            raise LactateThresholdNotSet
        if self.max_hr is None:
            raise MaxHrNotSet
        setattr(self, 'hr_zones', zones)

    def set_power_zones(self, zones: Zones) -> None:
        if self.ftp is None:
            raise FtpNotSet
        setattr(self, 'pw_zones', zones)
