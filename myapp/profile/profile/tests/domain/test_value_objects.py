import pytest
from profile.domain.value_objects import (
    Zones,
    ZonePercent,
    MainSport,
    Heigth,
    Ftp,
    MaxHr,
    LactateThr,
    )
from profile.application.use_cases import CreateUserProfileDto


def test_create_zone_success() -> None:
    zone = ZonePercent(20)
    assert str(zone) == '20%'


def test_create_zone_negative_failed() -> None:
    with pytest.raises(ValueError):
        ZonePercent(-40)


def test_create_zones() -> None:
    zone1 = ZonePercent(50)
    zone2 = ZonePercent(85)
    zone3 = ZonePercent(90)
    zone4 = ZonePercent(95)
    zone5 = ZonePercent(100)

    zones = Zones(zone1, zone2, zone3, zone4, zone5)
    str_rep = list(str(zones).split('/'))
    assert len(str_rep) == 5


def test_create_zones_illogical_sequence_faield():
    zone1 = ZonePercent(80)
    zone2 = ZonePercent(85)
    zone3 = ZonePercent(65)
    zone4 = ZonePercent(95)
    zone5 = ZonePercent(100)

    with pytest.raises(ValueError):
        Zones(zone1, zone2, zone3, zone4, zone5)


def test_create_zones_repeated_zone_failed():
    zone1 = ZonePercent(80)
    zone2 = ZonePercent(85)
    zone3 = ZonePercent(85)
    zone4 = ZonePercent(95)
    zone5 = ZonePercent(100)

    with pytest.raises(ValueError):
        Zones(zone1, zone2, zone3, zone4, zone5)


def test_create_main_sport_success() -> None:
    MainSport('cycling')


def test_create_main_sport_invalid() -> None:
    with pytest.raises(ValueError):
        MainSport('invalid')


def test_create_heigth_success() -> None:
    Heigth(154)


def test_create_heigth_incorrect_value() -> None:
    with pytest.raises(ValueError):
        Heigth(50)
        Heigth(250)
        Heigth('string')


def test_create_ftp_success():
    Ftp(300)


def test_create_ftp_not_a_number():
    with pytest.raises(ValueError):
        Ftp('string')


def test_create_max_hr_succes() -> None:
    MaxHr(195)


def test_create_max_hr_incorrect_value() -> None:
    with pytest.raises(ValueError):
        MaxHr('string')
        MaxHr(250)
        MaxHr(99)


def test_create_lactate_threshold_success() -> None:
    LactateThr(172)


def test_create_lactate_threshold_incorrect_value() -> None:
    with pytest.raises(ValueError):
        LactateThr('string')
