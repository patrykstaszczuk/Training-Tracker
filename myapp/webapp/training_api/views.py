from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import injector
from profile import (
    CreateUserProfile,
    CreateUserProfileDto,
)
from .serialization import serializers
# Create your views here.


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
