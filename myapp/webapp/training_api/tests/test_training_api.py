from django.test import TestCase
from django.contrib.auth.models import User
from training_api.models import Profile
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATING_PROFILE_URL = reverse('training_api:create-profile')


class TrainingApiTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test', password='password')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_creating_profile_endpoint(self) -> None:

        payload = {
            'main_sport': 'cycling',
            'weigth': 80,
            'heigth': 180,
        }
        res = self.client.post(CREATING_PROFILE_URL, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        profile = Profile.objects.get(user=self.user.id)
        self.assertEqual(profile.weigth, payload['weigth'])
