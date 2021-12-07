from dataclasses import dataclass
from profile.domain.value_objects import (
    UserId,
    Zones
    )
from profile.application.repositories import ProfileRepository


@dataclass(frozen=True)
class SetTrainingSpecificInformationDto:
    user_id: UserId
    height: int = None
    ftp: int = None
    max_hr: int = None
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
        attrs = {}
        for item in vars(input_dto):
            if getattr(input_dto, item):
                attrs.update({item: getattr(input_dto, item)})
        profile.update(**attrs)
        self.profile_repo.save(profile)
