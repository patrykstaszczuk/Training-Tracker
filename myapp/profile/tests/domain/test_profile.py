from django.test import TestCase
from profile import (
    ZonePercent,
    Zones,
    UserProfile,
)
from profile.domain.exceptions import (
    LactateThresholdNotSet
)


class UserProfileEntityTests(TestCase):

    def test_setting_training_zones_failed_lt_threshold_not_set(self):
        user = UserProfile(1, 'cycling')
        zones_list = [
            ZonePercent(50),
            ZonePercent(80),
            ZonePercent(85),
            ZonePercent(90),
            ZonePercent(95),
        ]
        zones = Zones(*zones_list)

        with self.assertRaises(LactateThresholdNotSet):
            user.set_hr_zones(zones)
