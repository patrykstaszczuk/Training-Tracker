import pytest
import datetime
from planner.domain.entities import AnnualPlan


@pytest.fixture()
def annual_plan() -> AnnualPlan:
    return AnnualPlan(
        user_id=1,
        start_date=datetime.date.today(),
        sport_discipline='cycling',
        volume=800,
    )


def test_should_return_proper_ending_date(annual_plan: AnnualPlan) -> None:
    start_date = annual_plan.start_date
    assert annual_plan.end_date == start_date + datetime.timedelta(365)
