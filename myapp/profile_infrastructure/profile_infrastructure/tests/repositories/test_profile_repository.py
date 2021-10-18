from django.contrib.auth.models import User
import pytest
from training_api.models import Profile
from profile_infrastructure.repositories.profile import DjangoProfileRepository
from profile.domain.entities import UserProfile


@pytest.fixture()
def repo() -> DjangoProfileRepository:
    return DjangoProfileRepository()


@pytest.fixture()
def user() -> User:
    return User.objects.create(username='test', password='password')

# def setUp(self):
#     self.repo = DjangoProfileRepository()
#     self.user = User.objects.create(username='test', password='password')


def test_creating_user_profile_success(repo: DjangoProfileRepository, user: User) -> None:
    profile = UserProfile(user_id=user.id, main_sport='cycling')
    repo.save(profile)


def test_retrieving_user_profile_success(user: User, repo: DjangoProfileRepository):
    obj = Profile.objects.create(user=user, main_sport='cycling')
    profile = repo.get(user.id)
    assert profile.main_sport == obj.main_sport


def test_user_profile_not_exits(repo: DjangoProfileRepository):
    with pytest.raises(Exception):
        repo.get(user_id=2)
