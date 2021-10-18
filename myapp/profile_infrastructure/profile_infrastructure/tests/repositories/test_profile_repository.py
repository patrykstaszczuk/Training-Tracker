from django.test import TestCase
from django.contrib.auth.models import User
from training_api.models import Profile
from profile_infrastructure.repositories.profile import DjangoProfileRepository
from profile.domain.entities import UserProfile


class ProfileRepositoryTests(TestCase):

    def setUp(self):
        self.repo = DjangoProfileRepository()
        self.user = User.objects.create(username='test', password='password')

    def test_creating_user_profile_success(self):
        profile = UserProfile(user_id=self.user.id, main_sport='cycling')
        self.repo.save(profile)

    def test_retrieving_user_profile_success(self):
        obj = Profile.objects.create(user=self.user, main_sport='cycling')
        profile = self.repo.get(self.user.id)
        self.assertEqual(profile.main_sport, obj.main_sport)

    def test_user_profile_not_exits(self):
        with self.assertRaises(Exception):
            self.repo.get(user_id=2)
