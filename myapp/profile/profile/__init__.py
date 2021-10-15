import injector
from profile.domain.entities import UserProfile
from profile.application.repositories import ProfileRepository
from profile.domain.value_objects import (
    ZonePercent,
    HrZones,
    PowerZones,
    UserId,
    MainSport,
    Weigth,
    Heigth,
    Ftp,
    MaxHr,
    LactateThr,
    )
from profile.application.use_cases import (
    SetTrainingZonesBoundary,
    SetTrainingZonesOutputDto,
    )
from profile.application.use_cases import (
    CreateUserProfile,
    CreateUserProfileDto,
)

__all__ = [
    #injector
    "Profile",
    # Entity
    "UserProfile",
    # repositories
    "ProfileRepository",
    # Value objects
    "UsersId",
    "HrZones",
    "PowerZones",
    "ZonePercent",
    "UserId",
    "MainSport",
    "Weigth",
    "Heigth",
    "Ftp",
    "MaxHr",
    "LactateThr",
    # user usecases
    "SetTrainingZonesBoundary",
    "CreateUserProfile",
    # input dto's
    "SetTrainingZonesOutputDto",
    "CreateUserProfileDto",
]


class Profile(injector.Module):
    @injector.provider
    def creating_profile_uc(
        self,
        repo: ProfileRepository
    ) -> CreateUserProfile:
        return CreateUserProfile(repo)