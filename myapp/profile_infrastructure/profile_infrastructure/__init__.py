from profile_infrastructure.repositories import InMemoryProfileRepository
# from users_infrastructure.queries import InMemoryGetUserTrainingProfile
from profile import ProfileRepository, UserProfile

import injector

__all__ = [
    "ProfileInfrastructure",
    # "InMemoryGetUserTrainingProfile",
]


class UsersInfrastructure(injector.Module):

    @injector.provider
    def users_repo(self) -> ProfileRepository:
        existing_profile = UserProfile(
            id=2,
            email="test@gmail.com",
            name='test',
            surname='test12345',
            main_sport='cycling',
        )
        repo = InMemoryProfileRepository()
        repo.save(existing_profile)
        return repo
