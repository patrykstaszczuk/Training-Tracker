from abc import ABC, abstractmethod
from dataclasses import dataclass
from profile.domain.value_objects import Zones, UserId
from typing import TypedDict


class ProfileDetails(TypedDict):
    main_sport: str
    weigth: int
    heigth: int
    ftp: int
    max_hr: int
    hr_zones: Zones
    pw_zones: Zones
    lactate_thr: int


class GetUserTrainingProfileDetails(ABC):

    @abstractmethod
    def query(self, user_id: UserId) -> ProfileDetails:
        pass
