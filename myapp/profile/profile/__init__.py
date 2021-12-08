import injector
from profile.domain.entities import UserProfile
from profile.application.repositories import ProfileRepository
from profile.domain.value_objects import (
    ProfileAttribute,
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
    CreateUserProfile,
    CreateUserProfileDto,
    SetTrainingSpecificInformation,
    SetTrainingSpecificInformationDto,
    SetHrTrainingZones,
    SetTrainingZonesDto,
    SetPowerTrainingZones,
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
    "ProfileAttribute",
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
    "CreateUserProfile",
    "SetTrainingSpecificInformation",
    "SetHrTrainingZones",
    "SetPowerTrainingZones",
    # input dtos
    "SetTrainingSpecificInformationDto",
    "CreateUserProfileDto",
    "SetTrainingZonesDto",
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

    @injector.provider
    def set_profile_information_uc(
        self,
        repo: ProfileRepository
    ) -> SetTrainingSpecificInformation:
        return SetTrainingSpecificInformation(repo)

    @injector.provider
    def set_hr_training_zones_uc(
        self,
        repo: ProfileRepository
    ) -> SetHrTrainingZones:
        return SetHrTrainingZones(repo)

    @injector.provider
    def set_power_training_zones_uc(
        self,
        repo: ProfileRepository
    ) -> SetPowerTrainingZones:
        return SetPowerTrainingZones(repo)
