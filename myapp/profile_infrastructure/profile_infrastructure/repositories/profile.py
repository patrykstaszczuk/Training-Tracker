from profile.application.repositories import ProfileRepository
import copy
from typing import Dict
from profile.domain.value_objects import UserId, Zones
from profile.domain.entities import UserProfile
import training_api


class DjangoProfileRepository(ProfileRepository):
    """ django db adapter """

    def __init__(self):
        self.profile_model = training_api.models.Profile.objects

    def get(self, user_id: UserId) -> UserProfile:
        try:
            profile_object = self.profile_model.get(
                user_id=user_id)
            return self._object_to_entity(profile_object)
        except self.profile_model.DoesNotExist:
            raise Exception('Profile not found')

    def save(self, profile: UserProfile) -> None:
        self.profile_model.create(**profile.__dict__)

    def _object_to_entity(self, profile_object: object) -> UserProfile:
        """ map django object attributes to entity attribute """
        profile = UserProfile(
            user_id=profile_object.user.id,
            main_sport=profile_object.main_sport,
            weigth=profile_object.weigth,
            heigth=profile_object.heigth,
            ftp=profile_object.ftp,
            max_hr=profile_object.max_hr,
            hr_zones=Zones.from_db_to_object(profile_object.hr_zones),
            pw_zones=Zones.from_db_to_object(profile_object.pw_zones),
            lactate_thr=profile_object.lactate_thr
        )

        return profile
