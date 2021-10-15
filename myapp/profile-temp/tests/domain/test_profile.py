from django.test import TestCase
from profile import (
    ZonePercent,
    PowerZones,
    HrZones,
    UserProfile,
)
from profile.domain.exceptions import (
    LactateThresholdNotSet,
    MaxHrNotSet,
    FtpNotSet,
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
        zones = HrZones(*zones_list)

        with self.assertRaises(LactateThresholdNotSet):
            user.set_hr_zones(zones)

    def test_setting_hr_zones_failed_max_hr_not_set(self):
        user = UserProfile(1, 'cycling', lactate_thr=172)
        zones_list = [
            ZonePercent(50),
            ZonePercent(80),
            ZonePercent(85),
            ZonePercent(90),
            ZonePercent(95),
        ]
        zones = HrZones(*zones_list)
        with self.assertRaises(MaxHrNotSet):
            user.set_hr_zones(zones)

    def test_setting_power_zones_failed_ftp_not_set(self):
        user = UserProfile(1, 'cycling')
        zones_list = [
            ZonePercent(50),
            ZonePercent(80),
            ZonePercent(85),
            ZonePercent(104),
            ZonePercent(105),
            ZonePercent(120),
        ]
        zones = PowerZones(*zones_list)
        with self.assertRaises(FtpNotSet):
            user.set_power_zones(zones)
