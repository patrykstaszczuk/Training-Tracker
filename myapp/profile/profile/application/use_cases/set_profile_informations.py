from dataclasses import dataclass
from profile.domain.value_objects import (
    UserId,
    Zones
    )
from profile.application.repositories import ProfileRepository


@dataclass(frozen=True)
class SetTrainingSpecificInformationDto:
    user_id: UserId
    heigth: int = None
    ftp: int = None
    max_hr: int = None
    hr_zones: Zones = None
    pw_zones: Zones = None
    lactate_thr: int = None


class SetTrainingSpecificInformation:
    """ setting additional information about user profile """

    def __init__(
        self,
        profile_repo: ProfileRepository,
    ) -> None:
        self.profile_repo = profile_repo

    def execute(self, input_dto: SetTrainingSpecificInformationDto) -> None:
        profile = self.profile_repo.get(input_dto.user_id)
        profile.update(
            heigth=input_dto.heigth,
            ftp=input_dto.ftp,
            max_hr=input_dto.max_hr,
            hr_zones=input_dto.hr_zones,
            pw_zones=input_dto.pw_zones,
            lactate_thr=input_dto.lactate_thr
        )
        self.profile_repo.save(profile)
