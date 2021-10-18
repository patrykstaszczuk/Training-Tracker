from health_diary.domain.value_objects import (
    Weigth,
    RestHr,
    StressScore,
    MoodScore,
    SleepLength,
)


class HealthDiary:
    def __init__(
        self,
        user_id: int,
        weigth: Weigth = None,
        rest_hr: RestHr = None,
        morning_sress_score: StressScore = None,
        evening_stress_score: StressScore = None,
        morning_mood: MoodScore = None,
        evening_mood: MoodScore = None,
        sleep_length: SleepLength = None,
    ) -> None:
        self.user_id = user_id
        self.weigth = weigth
        self.rest_hr = rest_hr
        self.morning_sress_score = morning_sress_score
        self.evening_stress_score = evening_stress_score
        self.moring_mood = morning_mood
        self.evening_mood = evening_mood
        self.sleep_length = sleep_length

    def set_attrs(self, **attrs):
        for attr in attrs:
            setattr(self, attr, attrs[attr])
