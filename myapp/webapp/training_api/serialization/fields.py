from rest_framework import serializers
from profile import (
    MainSport,
    Height,
    Ftp,
    MaxHr,
    LactateThr,
    ZonePercent,
    HrZones,
    PowerZones,
)


class CustomField(serializers.Field):
    def to_representation(self, value):
        return value


class MainSportField(CustomField):
    def to_internal_value(self, data):
        try:
            return MainSport(data)
        except ValueError as exc:
            raise serializers.ValidationError(exc)


class HeightField(CustomField):
    def to_internal_value(self, data):
        try:
            return Height(data)
        except ValueError as exc:
            raise serializers.ValidationError(exc)


class FtpField(CustomField):
    def to_internal_value(self, data):
        try:
            return Ftp(data)
        except ValueError as exc:
            raise serializers.ValidationError(exc)


class MaxHrField(CustomField):
    def to_internal_value(self, data):
        try:
            return MaxHr(data)
        except ValueError as exc:
            raise serializers.ValidationError(exc)


class LactateThrField(CustomField):
    def to_internal_value(self, data):
        try:
            return LactateThr(data)
        except ValueError as exc:
            raise serializers.ValidationError(exc)


class HrZonesField(CustomField):
    def to_internal_value(self, data):
        if not isinstance(data, list):
            raise serializers.ValidationError('Must be a list of values')
        zones_percent = []
        for zone in data:
            try:
                zones_percent.append(ZonePercent(zone))
            except ValueError as exc:
                raise serializers.ValidationError(exc)
        try:
            return HrZones(*zones_percent)
        except ValueError as exc:
            raise serializers.ValidationError(exc)
