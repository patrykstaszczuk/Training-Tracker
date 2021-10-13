from users.application.repositories import UsersRepository
import copy
from typing import Dict
from users.domain.value_objects import UserId
from users.domain.entities import User


class InMemoryUserRepository(UsersRepository):
    """ in memory db implementation for testing purpose """

    def __init__(self) -> None:
        self._storage: Dict[UserId, User] = {}

    def get(self, user_id: UserId) -> User:
        return copy.deepcopy(self._storage[user_id])

    def save(self, user: User) -> None:
        self._storage[user] = copy.deepcopy(user)
