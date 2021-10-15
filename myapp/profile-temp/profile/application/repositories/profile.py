from abc import ABC, abstractmethod
from profile.domain.value_objects import UserId
from profile.domain.entities import UserProfile
import copy
from typing import Dict


class ProfileRepository(ABC):
    """ abstract repository for users """

    @abstractmethod
    def get(self, user_id: UserId) -> UserProfile:
        pass

    @abstractmethod
    def save(self, user: UserProfile) -> None:
        pass


class InMemoryProfileRepository(ProfileRepository):
    """ in memory db implementation for testing purpose """

    def __init__(self) -> None:
        self._storage: Dict[UserId, UserProfile] = {}

    def get(self, user_id: UserId) -> UserProfile:
        return copy.deepcopy(self._storage[user_id])

    def save(self, profile: UserProfile) -> None:
        self._storage[profile.user_id] = copy.deepcopy(profile)
