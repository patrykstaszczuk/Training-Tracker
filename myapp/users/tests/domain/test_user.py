from django.test import TestCase
from users import (
    ZonePercent,
    Zones,
    User,
)
from users.domain.exceptions import (
    LactateThresholdNotSet
)


class UserEntityTests(TestCase):

    def test_setting_training_zones_failed_lt_threshold_not_set(self):
        user = User(1, 'test@gmail.com', 'name', 'surname',
                    'password', 'cycling')
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
