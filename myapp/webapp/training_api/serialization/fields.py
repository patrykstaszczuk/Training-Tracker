from rest_framework import serializers
from profile import (
    MainSport,
    Heigth,
    Ftp,
    MaxHr,
    LactateThr,
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


class HeigthField(CustomField):
    def to_internal_value(self, data):
        try:
            return Heigth(data)
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
