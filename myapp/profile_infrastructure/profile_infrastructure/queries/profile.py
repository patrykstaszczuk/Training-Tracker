from dataclasses import dataclass
from rest_framework import serializers
from profile import (
    UserId,
    )
from profile.application.queries import (
    ProfileDetails,
    GetUserTrainingProfileDetails
    )
from profile.domain.value_objects import Zones
import training_api


class DjangoGetUserTrainingProfile(GetUserTrainingProfileDetails):

    def query(self, user_id: UserId) -> ProfileDetails:
        profile = training_api.models.Profile.objects.get(user_id=user_id)
        return _row_to_typed_dict(profile)


def _row_to_typed_dict(profile: object) -> ProfileDetails:
    dict = ProfileDetails(
        user_id=profile.user.id,
        main_sport=profile.main_sport,
        heigth=profile.heigth,
        ftp=profile.ftp,
        max_hr=profile.max_hr,
        hr_zones=Zones.from_db_to_object(profile.hr_zones),
        pw_zones=Zones.from_db_to_object(profile.pw_zones),
        lactate_thr=profile.lactate_thr
    )
    return dict
#
# def object_to_dto(object: QuerySet) -> UsersDto:
#     pass
#     #
    # class InMemoryGetUserTrainingProfile(GetUserTrainingProfile):
    #
    #     def __init__(
    #         self,
    #         repo: InMemoryUserRepository
    #     ) -> None:
    #         self.repo = repo
    #
    #     def query(self, user_id: UserId) -> UsersDto:
    #         return self.repo.get(user_id)
    #
    #
    #
    #
    # def queryset_to_dto(queryset: QuerySet):
