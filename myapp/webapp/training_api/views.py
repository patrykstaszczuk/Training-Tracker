from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import injector

from profile import (
    CreateUserProfile,
    CreateUserProfileDto,
    GetUserTrainingProfileDetails,
    SetTrainingSpecificInformation,
    SetTrainingSpecificInformationDto,
    SetHrTrainingZones,
    SetPowerTrainingZones,
    SetTrainingZonesDto,
)
from .serialization import serializers


class BaseAuthPermClass:
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class CreateProfileApi(BaseAuthPermClass, APIView):

    @injector.inject
    def setup(
        self,
        request,
        creating_profile_uc: CreateUserProfile,
        **kwargs
    ) -> None:
        self.creating_profile_uc = creating_profile_uc
        super().setup(request, kwargs)

    def post(self, request, *args, **kwargs):
        serializer = serializers.CreateProfileSerializer(data=request.data)
        if serializer.is_valid():
            dto = CreateUserProfileDto(
                user_id=request.user.id, **serializer.data)
            self.creating_profile_uc.execute(dto)
            return Response(status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApi(BaseAuthPermClass, APIView):

    @injector.inject
    def setup(
        self,
        request,
        get_user_profile_query: GetUserTrainingProfileDetails,
        set_profile_information_uc: SetTrainingSpecificInformation,
        **kwargs
    ) -> None:
        self.get_user_profile_query = get_user_profile_query
        self.set_profile_information_uc = set_profile_information_uc
        super().setup(request, kwargs)

    def get(self, request, *args, **kwargs):
        data = self.get_user_profile_query.query(request.user.id)
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = serializers.SetTrainingSpecificInformationSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        dto = SetTrainingSpecificInformationDto(
            user_id=request.user.id,
            height=serializer.data.get('height'),
            ftp=serializer.data.get('ftp'),
            max_hr=serializer.data.get('max_hr'),
            lactate_thr=serializer.data.get('lactate_thr')
        )
        self.set_profile_information_uc.execute(dto)
        return Response(status=status.HTTP_200_OK)


class SetHeartRateZones(BaseAuthPermClass, APIView):

    @injector.inject
    def setup(
        self,
        request,
        set_heart_rate_zones: SetHrTrainingZones,
        **kwargs
    ) -> None:
        self.set_heart_rate_zones = set_heart_rate_zones
        super().setup(request, kwargs)

    def post(self, request, *args, **kwargs):
        serializer = serializers.SettingTrainingZonesSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        dto = SetTrainingZonesDto(
            user_id=request.user.id,
            zones=serializer.data.get('zones')
        )
        self.set_heart_rate_zones.execute(dto)
        return Response(status=status.HTTP_200_OK)
