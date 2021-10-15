from profile_infrastructure.repositories import DjangoProfileRepository
# from users_infrastructure.queries import InMemoryGetUserTrainingProfile
from profile import ProfileRepository, UserProfile

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
