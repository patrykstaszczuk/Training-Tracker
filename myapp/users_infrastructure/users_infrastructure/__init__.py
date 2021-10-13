from users_infrastructure.repositories import InMemoryUserRepository
from users import UsersRepository, User

import injector

__all__ = [
    "UsersInfrastructure",
]


class UsersInfrastructure(injector.Module):

    @injector.provider
    def users_repo(self) -> UsersRepository:
        existing_user = User(
            id=2,
            email="test@gmail.com",
            name='test',
            surname='test12345',
            main_sport='cycling',
        )
        repo = InMemoryUserRepository()
        repo.save(existing_user)
        return repo
