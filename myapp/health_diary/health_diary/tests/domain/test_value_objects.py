import pytest
from health_diary.domain.value_objects import (
        Weigth,
        RestHr,
        StressScore,
        MoodScore,
        SleepLength,
)


def test_Weigth() -> None:
    Weigth(72)
    with pytest.raises(ValueError):
        Weigth(19)
    with pytest.raises(ValueError):
        Weigth(350)


def test_RestHr() -> None:
    RestHr(50)
    with pytest.raises(ValueError):
        RestHr(29)
    with pytest.raises(ValueError):
        RestHr(100)


def test_StressScore() -> None:
    StressScore(7)
    with pytest.raises(ValueError):
        StressScore(-1)
    with pytest.raises(ValueError):
        StressScore(11)


def test_MoodScore() -> None:
    MoodScore(7)
    with pytest.raises(ValueError):
        MoodScore(-1)
    with pytest.raises(ValueError):
        MoodScore(11)


def test_SleepLength() -> None:
    SleepLength("07:00:00")


def test_SleepLength_invalid_format() -> None:
    with pytest.raises(ValueError):
        SleepLength("0dsa3:223323:2323")


def test_SleepLength_invalid_arg() -> None:
    with pytest.raises(ValueError):
        SleepLength(12354)


def test_SleepLength_too_long() -> None:
    with pytest.raises(ValueError):
        SleepLength("21:0:0")
