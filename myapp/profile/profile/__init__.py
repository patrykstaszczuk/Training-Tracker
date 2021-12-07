import injector
from profile.domain.entities import UserProfile
from profile.application.repositories import ProfileRepository
from profile.domain.value_objects import (
    ZonePercent,
    HrZones,
    PowerZones,
    UserId,
    MainSport,
    Height,
    Ftp,
    MaxHr,
    LactateThr,
    )
from profile.application.use_cases import (
    SetTrainingZonesBoundary,
    SetTrainingZonesOutputDto,
    CreateUserProfile,
    CreateUserProfileDto,
    SetTrainingSpecificInformation,
    SetTrainingSpecificInformationDto,
    )
from profile.application.queries import (
    GetUserTrainingProfileDetails,
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
    "Height",
    "Ftp",
    "MaxHr",
    "LactateThr",
    # use cases
    "SetTrainingZonesBoundary",
    "CreateUserProfile",
    "SetTrainingSpecificInformation",
    # input dtos
    "SetTrainingZonesOutputDto",
    "SetTrainingSpecificInformationDto",
    "CreateUserProfileDto",
    # queries
    "GetUserTrainingProfileDetails",
]


class Profile(injector.Module):
    @injector.provider
    def creating_profile_uc(
        self,
        repo: ProfileRepository
    ) -> CreateUserProfile:
        return CreateUserProfile(repo)
