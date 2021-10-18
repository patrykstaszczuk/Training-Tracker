from profile_infrastructure.repositories import DjangoProfileRepository
from profile_infrastructure.queries import DjangoGetUserTrainingProfile
# from users_infrastructure.queries import InMemoryGetUserTrainingProfile
from profile import (
    ProfileRepository,
    UserProfile,
    GetUserTrainingProfileDetails,
    )
import injector

__all__ = [
    #injector
    "ProfileInfrastructure",
    # "InMemoryGetUserTrainingProfile",
]


class ProfileInfrastructure(injector.Module):

    @injector.provider
    def profile_repo(self) -> ProfileRepository:
        return DjangoProfileRepository()

    @injector.provider
    def retrieve_profile(self) -> GetUserTrainingProfileDetails:
        return DjangoGetUserTrainingProfile()
