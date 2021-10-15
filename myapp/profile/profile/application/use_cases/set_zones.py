from dataclasses import dataclass
from profile.domain.value_objects import (
    UserId,
    Zones,
    ZonePercent,
    )
from profile.application.repositories import ProfileRepository
from abc import ABC, abstractmethod
from typing import Tuple, List


@dataclass(frozen=True)
class SetTrainingZonesDto:
    user_id: UserId
    zones: Zones


@dataclass(frozen=True)
class SetTrainingZonesOutputDto:
    zones: List[Tuple[ZonePercent, int]]


class SetTrainingZonesBoundary:
    @abstractmethod
    def present(self, output_dto: SetTrainingZonesOutputDto) -> None:
        pass


class SetTrainingZones(ABC):

    def __init__(
        self,
        profile_repo: ProfileRepository,
    ) -> None:
        self.profile_repo = profile_repo

    @abstractmethod
    def execute(self, input_dto: SetTrainingZonesDto) -> None:
        pass


class SetHrTrainingZones(SetTrainingZones):

    def execute(self, input_dto: SetTrainingZonesDto) -> None:
        user = self.profile_repo.get(input_dto.user_id)
        user.set_hr_zones(input_dto.zones)
        self.profile_repo.save(user)
        #
        # zones = user.calculate_hr_zones_based_on_lactate_threshold()
        # output_dto = SetTrainingZonesOutputDto(zones)
        # self.output_boundary.present(output_dto)


class SetPowerTrainingZones(SetTrainingZones):

    def execute(self, input_dto: SetTrainingZonesDto) -> None:
        user = self.profile_repo.get(input_dto.user_id)
        user.set_power_zones(input_dto.zones)
        self.profile_repo.save(user)
        #
        # zones = user.calculate_power_zones_based_on_ftp()
        # output_dto = SetTrainingZonesOutputDto(zones)
        # self.output_boundary.present(output_dto)
