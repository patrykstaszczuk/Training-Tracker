from django.test import TestCase
from django.contrib.auth.models import User
from training_api.models import Profile
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATING_PROFILE_URL = reverse('training_api:profile-create')
RETRIEVE_PROFILE_URL = reverse('training_api:profile')


class TrainingApiTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test', password='password')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_creating_profile_endpoint(self) -> None:

        payload = {
            'main_sport': 'cycling',
            'height': 180,
        }
        res = self.client.post(CREATING_PROFILE_URL, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        profile = Profile.objects.get(user=self.user.id)
        self.assertEqual(profile.height, payload['height'])

    def test_retrieving_profile_endpoint(self) -> None:
        profile = Profile.objects.create(
            user_id=self.user.id,
            main_sport='cycling'
            )

        res = self.client.get(RETRIEVE_PROFILE_URL, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['user_id'], profile.user_id)
