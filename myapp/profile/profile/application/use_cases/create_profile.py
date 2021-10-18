from dataclasses import dataclass
from profile.domain.value_objects import (
    Zones,
    MainSport,
    Heigth,
    Ftp,
    MaxHr,
    LactateThr,
    )
from profile.application.repositories import ProfileRepository
from profile.domain.entities import UserProfile


@dataclass
class CreateUserProfileDto:
    user_id: int
    main_sport: MainSport
    heigth: Heigth = None
    ftp: Ftp = None
    max_hr: MaxHr = None
    lactate_thr: LactateThr = None


class CreateUserProfile:

    def __init__(
        self,
        profile_repo: ProfileRepository,
    ) -> None:
        self.repo = profile_repo

    def execute(self, input_dto: CreateUserProfileDto) -> None:
        attrs = {key: item.value for (key, item) in vars(
            input_dto).items() if item is not None and not isinstance(item, int)}
        profile = UserProfile.create(input_dto.user_id, attrs)
        self.repo.save(profile)
