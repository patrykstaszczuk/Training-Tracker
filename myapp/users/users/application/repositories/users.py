from abc import ABC, abstractmethod
from users.domain.value_objects import UserId
from users.domain.entities import User
import copy
from typing import Dict


class UsersRepository(ABC):
    """ abstract repository for users """

    @abstractmethod
    def get(self, user_id: UserId) -> User:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass


class InMemoryUserRepository(UsersRepository):
    """ in memory db implementation for testing purpose """

    def __init__(self) -> None:
        self._storage: Dict[UserId, User] = {}

    def get(self, user_id: UserId) -> User:
        return copy.deepcopy(self._storage[user_id])

    def save(self, user: User) -> None:
        self._storage[user.id] = copy.deepcopy(user)
