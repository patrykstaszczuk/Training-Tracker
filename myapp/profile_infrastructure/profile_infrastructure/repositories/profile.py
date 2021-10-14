from profile.application.repositories import ProfileRepository
import copy
from typing import Dict
from profile.domain.value_objects import UserId
from profile.domain.entities import UserProfile


class InMemoryProfileRepository(ProfileRepository):
    """ in memory db implementation for testing purpose """

    def __init__(self) -> None:
        self._storage: Dict[UserId, UserProfile] = {}

    def get(self, user_id: UserId) -> UserProfile:
        return copy.deepcopy(self._storage[user_id])

    def save(self, profile: UserProfile) -> None:
        self._storage[profile.user_id] = copy.deepcopy(profile)
