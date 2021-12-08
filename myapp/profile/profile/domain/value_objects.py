from typing import Union
from abc import ABC, abstractmethod
UserId = int


class ZonePercent:
    def __init__(
        self,
        value: int,
    ):
        try:
            value = int(value)
        except ValueError:
            raise ValueError('Zone percent must be a number')
        if value < 0:
            raise ValueError('Zone percent cannot be negative')
        self._value = value

    @property
    def value(self):
        return self._value

    def __str__(self):
        return f"{self._value}%"


class Zones(ABC):
    def __init__(self,
                 zone1: ZonePercent,
                 zone2: ZonePercent,
                 zone3: ZonePercent,
                 zone4: ZonePercent,
                 zone5: ZonePercent,
                 *args,
                 ):
        self._zone1 = zone1.value
        self._zone2 = zone2.value
        self._zone3 = zone3.value
        self._zone4 = zone4.value
        self._zone5 = zone5.value

        self._validate_sequence()

    def _validate_sequence(self):
        zones_list = list(vars(self).values())
        for i, j in enumerate(zones_list[: -1]):
            if j >= zones_list[i+1]:
                raise ValueError('Set proper value for next zone')

    def __str__(self):
        string_rep = ''
        for attr in vars(self).values():
            string_rep += str(attr) + '/'
        return string_rep[:-1]

    @staticmethod
    @abstractmethod
    def from_db_to_object(zones_as_string: str) -> 'Zones':
        """ convert string representation of zones to object """
        pass


class HrZones(Zones):
    pass

    @staticmethod
    def from_db_to_object(zones_as_string: str) -> 'Zones':
        """ convert string representation of zones to object """
        if zones_as_string is None:
            return
        raw_zones = list(zones_as_string.split("/"))
        return HrZones(*[ZonePercent(zone) for zone in raw_zones])


class PowerZones(Zones):
    def __init__(self,
                 zone1: ZonePercent,
                 zone2: ZonePercent,
                 zone3: ZonePercent,
                 zone4: ZonePercent,
                 zone5: ZonePercent,
                 zone6: ZonePercent,
                 *args,
                 ):
        super().__init__(zone1, zone2, zone3, zone4, zone5)
        self._zone6 = zone6.value

    @staticmethod
    def from_db_to_object(zones_as_string: str) -> 'Zones':
        """ convert string representation of zones to object """
        if zones_as_string is None:
            return
        raw_zones = list(zones_as_string.split("/"))
        return PowerZones(*[ZonePercent(zone) for zone in raw_zones])


class ProfileAttribute(ABC):
    def __init__(
        self,
        value: Union[str, int],
    ) -> None:
        self.__set__(self, value)

    def __get__(self, obj: 'ProfileAttribute') -> Union[int, str]:
        return self._value

    @property
    def value(self) -> Union[int, str]:
        return self._value

    @abstractmethod
    def __set__(self, obj: 'ProfileAttribute', value: Union[int, str]) -> None:
        pass


class MainSport(ProfileAttribute):
    def __set__(self, obj, value) -> None:
        if value.lower() not in ['triathlon', 'cycling']:
            raise ValueError(
                'Invalid main sport, should be either "triathlon" or "cycling"'
            )
        self._value = value.lower()


class Height(ProfileAttribute):
    def __set__(self, obj, value) -> None:
        if not isinstance(value, int):
            raise ValueError('Provide a number')
        if not 50 < value < 250:
            raise ValueError('Incorrect heigth')
        self._value = value


class Ftp(ProfileAttribute):
    def __set__(self, obj, value) -> None:
        if not isinstance(value, int):
            raise ValueError('Provide a number')
        self._value = value


class MaxHr(ProfileAttribute):
    def __set__(self, obj, value) -> None:
        if not isinstance(value, int):
            raise ValueError('Provide a number')
        if not 100 < value < 250:
            raise ValueError('Incorrect max heart rate')
        self._value = value


class LactateThr(ProfileAttribute):
    def __set__(self, obj, value) -> None:
        if not isinstance(value, int):
            raise ValueError('Provide a number')
        self._value = value
