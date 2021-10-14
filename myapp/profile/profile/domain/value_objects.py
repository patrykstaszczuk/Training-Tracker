UserId = int


class ZonePercent:
    def __init__(
        self,
        value: int,
    ):
        if value < 0:
            raise ValueError('Zone percent cannot be negative')
        if value > 100:
            raise ValueError('Zone percentage cannot exceed 100%')

        self._value = value

    @property
    def value(self):
        return self._value

    def __str__(self):
        return f"{self._value}%"


class Zones:
    def __init__(self,
                 zone1: ZonePercent,
                 zone2: ZonePercent,
                 zone3: ZonePercent,
                 zone4: ZonePercent,
                 zone5: ZonePercent,
                 ):
        self._zone1 = zone1.value
        self._zone2 = zone2.value
        self._zone3 = zone3.value
        self._zone4 = zone4.value
        self._zone5 = zone5.value

        zones_list = list(vars(self).values())
        for i, j in enumerate(zones_list[: -1]):
            if j >= zones_list[i+1]:
                raise ValueError('Set proper value for next zone')

    def __str__(self):
        return f"{self._zone1}/{self._zone2}/{self._zone3}/{self._zone4}/{self._zone5}"

    @staticmethod
    def from_db_to_object(zones_as_string: str):
        """ convert string representation of zones to object """
        raw_zones = list(zones_as_string.split("/"))
        return Zones(raw_zones[0], raw_zones[1], raw_zones[2], raw_zones[3],
                     raw_zones[4])
