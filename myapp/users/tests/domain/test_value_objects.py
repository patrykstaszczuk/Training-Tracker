from django.test import TestCase
from users.domain.value_objects import Zones, ZonePercent


class ValueObjectsTests(TestCase):

    def test_create_zone_success(self) -> None:
        zone = ZonePercent(20)
        self.assertEqual(str(zone), '20%')

    def test_create_zone_negative_failed(self) -> None:
        with self.assertRaises(ValueError):
            ZonePercent(-40)

    def test_create_zone_greater_then_100_failed(self) -> None:
        with self.assertRaises(ValueError):
            ZonePercent(101)

    def test_create_zones(self) -> None:
        zone1 = ZonePercent(50)
        zone2 = ZonePercent(85)
        zone3 = ZonePercent(90)
        zone4 = ZonePercent(95)
        zone5 = ZonePercent(100)

        zones = Zones(zone1, zone2, zone3, zone4, zone5)
        str_rep = list(str(zones).split('/'))
        self.assertEqual(len(str_rep), 5)

    def test_create_zones_illogical_sequence_faield(self):
        zone1 = ZonePercent(80)
        zone2 = ZonePercent(85)
        zone3 = ZonePercent(65)
        zone4 = ZonePercent(95)
        zone5 = ZonePercent(100)

        with self.assertRaises(ValueError):
            Zones(zone1, zone2, zone3, zone4, zone5)

    def test_create_zones_repeated_zone_failed(self):
        zone1 = ZonePercent(80)
        zone2 = ZonePercent(85)
        zone3 = ZonePercent(85)
        zone4 = ZonePercent(95)
        zone5 = ZonePercent(100)

        with self.assertRaises(ValueError):
            Zones(zone1, zone2, zone3, zone4, zone5)
