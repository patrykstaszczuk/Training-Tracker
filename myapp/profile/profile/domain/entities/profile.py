from profile.domain.value_objects import Zones
from profile.domain.exceptions import (
    IncorrectMainSport,
    LactateThresholdNotSet,
    MaxHrNotSet,
)


class UserProfile:
    def __init__(
        self,
        user_id: int,
        main_sport: str,
        weigth: int = None,
        heigth: int = None,
        ftp: int = None,
        max_hr: int = None,
        hr_zones: Zones = None,
        pw_zones: Zones = None,
        lactate_thr: int = None,

    ) -> None:
        self.user_id = user_id
        self.main_sport = main_sport
        self.weigth = weigth
        self.heigth = heigth
        self.ftp = ftp
        self.max_hr = max_hr
        self.hr_zones = hr_zones
        self.pw_zones = pw_zones
        self.lactate_thr = lactate_thr

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
