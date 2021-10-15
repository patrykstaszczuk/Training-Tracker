from django.test import TestCase
from profile.domain.value_objects import (
    Zones,
    ZonePercent,
    MainSport,
    Weigth,
    Heigth,
    Ftp,
    MaxHr,
    LactateThr,
    )
from profile.application.use_cases import CreateUserProfileDto


class ValueObjectsTests(TestCase):

    def test_create_zone_success(self) -> None:
        zone = ZonePercent(20)
        self.assertEqual(str(zone), '20%')

    def test_create_zone_negative_failed(self) -> None:
        with self.assertRaises(ValueError):
            ZonePercent(-40)

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

    def test_create_main_sport_success(self) -> None:
        MainSport('cycling')

    def test_create_main_sport_invalid(self) -> None:
        with self.assertRaises(ValueError):
            MainSport('invalid')

    def test_create_int_weigth_success(self) -> None:
        Weigth(60)
        Weigth(200.23)

    def test_create_weigth_too_low(self) -> None:
        with self.assertRaises(ValueError):
            Weigth(20)

    def test_create_weigth_too_high(self) -> None:
        with self.assertRaises(ValueError):
            Weigth(301)

    def test_create_heigth_success(self) -> None:
        Heigth(154)

    def test_create_heigth_incorrect_value(self) -> None:
        with self.assertRaises(ValueError):
            Heigth(50)
            Heigth(250)
            Heigth('string')

    def test_create_ftp_success(self):
        Ftp(300)

    def test_create_ftp_not_a_number(self):
        with self.assertRaises(ValueError):
            Ftp('string')

    def test_create_max_hr_succes(self) -> None:
        MaxHr(195)

    def test_create_max_hr_incorrect_value(self) -> None:
        with self.assertRaises(ValueError):
            MaxHr('string')
            MaxHr(250)
            MaxHr(99)

    def test_create_lactate_threshold_success(self) -> None:
        LactateThr(172)

    def test_create_lactate_threshold_incorrect_value(self) -> None:
        with self.assertRaises(ValueError):
            LactateThr('string')
