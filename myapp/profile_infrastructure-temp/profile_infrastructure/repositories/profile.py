from profile.application.repositories import ProfileRepository
import copy
from typing import Dict
from profile.domain.value_objects import UserId
from profile.domain.entities import UserProfile
import training_api


class DjangoProfileRepository(ProfileRepository):
    """ django db adapter """

    def get(self, user_id: UserId) -> UserProfile:
        pass

    def save(self, profile: UserProfile) -> None:
        training_api.models.Profile.objects.create(**profile.__dict__)
