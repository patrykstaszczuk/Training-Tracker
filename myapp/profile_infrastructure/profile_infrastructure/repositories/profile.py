import training_api
from profile.application.repositories import ProfileRepository
from profile.domain.value_objects import UserId, Zones, ProfileAttribute
from profile.domain.entities import UserProfile


class DjangoProfileRepository(ProfileRepository):
    """ django db adapter """

    def __init__(self):
        self.profile_model = training_api.models.Profile

    def get(self, user_id: UserId) -> UserProfile:
        try:
            profile_object = self.profile_model.objects.get(
                user_id=user_id)
            return self._object_to_entity(profile_object)
        except self.profile_model.DoesNotExist:
            raise Exception('Profile not found')

    def save(self, profile: UserProfile) -> None:
        if profile.id:
            profile_object = self.profile_model.objects.get(
                id=profile.id, user_id=profile.user_id)
            for item in vars(profile):
                if isinstance(getattr(profile, item), ProfileAttribute):
                    value_object = getattr(profile, item)
                    setattr(profile_object, item, value_object.value)
                else:
                    setattr(profile_object, item, getattr(profile, item))
            profile_object.save()
        else:
            self.profile_model.objects.create(
                user_id=profile.user_id,
                main_sport=profile.main_sport,
                height=profile.height,
                ftp=profile.ftp,
                max_hr=profile.max_hr,
                lactate_thr=profile.lactate_thr
                )

    def _object_to_entity(self, profile_object: object) -> UserProfile:
        """ map django object attributes to entity attribute """
        profile = UserProfile(
            user_id=profile_object.user.id,
            main_sport=profile_object.main_sport,
            id=profile_object.id,
            height=profile_object.height,
            ftp=profile_object.ftp,
            max_hr=profile_object.max_hr,
            hr_zones=Zones.from_db_to_object(profile_object.hr_zones),
            pw_zones=Zones.from_db_to_object(profile_object.pw_zones),
            lactate_thr=profile_object.lactate_thr
        )

        return profile
