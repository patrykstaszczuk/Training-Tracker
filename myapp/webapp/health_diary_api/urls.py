from django.urls import path
from . import views

app_name = 'health_diary_api'

urlpatterns = [
    path('', views.HealthDiaryApi.as_view(), name='health-diary'),
    path('<date>', views.HealthDiaryDetailApi.as_view(),
         name='health-diary-detail'),

]
