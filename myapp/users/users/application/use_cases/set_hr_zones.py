from dataclasses import dataclass
from users.domain.value_objects import (
    UserId,
    Zones,
    ZonePercent,
    )
from users.application.repositories import UsersRepository
from users.domain.entities import User
from abc import ABC, abstractmethod
from typing import Tuple, List


@dataclass(frozen=True)
class SetHrTrainingZonesDto:
    id: UserId
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
        users_repo: UsersRepository,
    ) -> None:
        self.output_boundary = output_boundary
        self.users_repo = users_repo

    def execute(self, input_dto: SetHrTrainingZonesDto) -> None:
        user = self.users_repo.get(input_dto.id)
        user.set_hr_zones(input_dto.zones)
        self.users_repo.save(user)

        zones = user.calculate_hr_zones_based_on_lactate_threshold()
        output_dto = SetHrTrainingZonesOutputDto(zones)
        self.output_boundary.present(output_dto)
