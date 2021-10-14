from django.contrib.auth import models, authenticate
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status, serializers


class CreateAccountAPI(APIView):

    class CreateUserSerializer(serializers.ModelSerializer):

        class Meta:
            model = models.User
            fields = ('username', 'password')
            extra_kwargs = {"password": {"write_only": True}, }

        def save(self, **kwargs):
            user = models.User.objects.create(
                username=self.validated_data['username'])
            user.set_password(self.validated_data['password'])
            user.save()

    def post(self, request, *args, **kwargs):
        serializer = self.CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )


class GetTokenAPI(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
