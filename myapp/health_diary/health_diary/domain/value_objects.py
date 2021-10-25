from abc import ABC, abstractmethod
from typing import Union
import datetime


class HealthDiaryAttribute(ABC):
    def __init__(self, value):
        self.validate(value)
        self._value = value

    @property
    def value(self):
        return self._value

    @abstractmethod
    def validate(self, value: Union[str, int]) -> None:
        pass


class Weigth(HealthDiaryAttribute):
    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError('Must be a number')
        if not 19 < value < 350:
            raise ValueError('Must be in range <21:349>')
        self._value = value


class RestHr(HealthDiaryAttribute):
    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError('Must be a number')
        if not 29 < value < 100:
            raise ValueError('Must be in range <30:99>')
        self._value = value


class StressScore(HealthDiaryAttribute):
    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError('Must be a number')
        if value < 0:
            raise ValueError('Must not be negative')
        if value > 10:
            raise ValueError('Must be within <0:10> range')
        self._value = value


class MoodScore(StressScore):
    pass


class SleepLength(HealthDiaryAttribute):
    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError("Must be a string")
        value = datetime.datetime.strptime(value, "%H:%M:%S")
        if not 0 < value.hour < 21:
            raise ValueError('Must be within <0:20>')
        self._value = value
