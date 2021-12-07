import injector
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from health_diary import (
    GettingDailyStatistics,
    GettingListOfDiaries,
)
# Create your views here.


class BaseAuthPermClass:
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class HealthDiaryApi(BaseAuthPermClass, APIView):

    @injector.inject
    def setup(
        self,
        request,
        get_list_of_diaries: GettingListOfDiaries,
        **kwargs
    ) -> None:
        self.get_list_of_diaries = get_list_of_diaries
        super().setup(request, kwargs)

    def get(self, request, *args, **kwargs):
        data = self.get_list_of_diaries.query(user_id=request.user.id)
        return Response(data=data, status=status.HTTP_200_OK)


class HealthDiaryDetailApi(BaseAuthPermClass, APIView):
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
        date = kwargs.get('date')
        data = self.get_daily_statistic_uc.query(request.user.id, date)
        return Response(data=data, status=status.HTTP_200_OK)
