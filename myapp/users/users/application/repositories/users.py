from abc import ABC, abstractmethod
from users.domain.value_objects import UserId
from users.domain.entities.domain import User


class UsersRepository(ABC):
    """ abstract repository for users """

    @abstractmethod
    def get(self, user_id: UserId) -> User:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass
