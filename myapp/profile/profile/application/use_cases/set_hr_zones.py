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
class SetHrTrainingZonesDto:
    user_id: UserId
    zones: Zones


@dataclass(frozen=True)
class SetHrTrainingZonesOutputDto:
    zones: List[Tuple[ZonePercent, int]]


class SetHrTrainingZonesBoundary(ABC):
    @abstractmethod
    def present(self, output_dto: SetHrTrainingZonesOutputDto) -> None:
        pass


class SetHrTrainingZones:

    def __init__(
        self,
        output_boundary: SetHrTrainingZonesBoundary,
        profile_repo: ProfileRepository,
    ) -> None:
        self.output_boundary = output_boundary
        self.profile_repo = profile_repo

    def execute(self, input_dto: SetHrTrainingZonesDto) -> None:
        user = self.profile_repo.get(input_dto.user_id)
        user.set_hr_zones(input_dto.zones)
        self.profile_repo.save(user)

        zones = user.calculate_hr_zones_based_on_lactate_threshold()
        output_dto = SetHrTrainingZonesOutputDto(zones)
        self.output_boundary.present(output_dto)
