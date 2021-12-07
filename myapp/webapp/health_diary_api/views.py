import injector
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from health_diary import (
    GettingDailyStatistics,
)
# Create your views here.


class BaseAuthPermClass:
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class HealthDiaryApi(APIView):

    @injector.inject
    def setup(
        self,
        request,
        get_daily_statistic_uc: GettingDailyStatistics,
        **kwargs
    ) -> None:
        self.get_daily_statistic_uc = get_daily_statistic_uc
        super().setup(request, kwargs)

    def get(self, request, *args, **kwargs):
        pass
