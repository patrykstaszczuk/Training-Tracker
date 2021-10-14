from dataclasses import dataclass
from rest_framework import serializers
from profile import (
    UserId,
    )
from profile.application.queries import ProfileDto, GetUserTrainingProfile
from profile_infrastructure.repositories import InMemoryProfileRepository


class DjangoGetUserTrainingProfile(GetUserTrainingProfile):

    def query(self, user_id: UserId) -> ProfileDto:
        pass

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
