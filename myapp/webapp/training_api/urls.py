from django.urls import path
from . import views

app_name = 'training_api'

urlpatterns = [
    path('create/', views.CreateProfileApi.as_view(),
         name='profile-create'),
    path('', views.ProfileApi.as_view(), name='profile'),
    path('set-zones/hr', views.SetHeartRateZones.as_view(), name='set-zones-hr'),
    # path('set-zones/pw', views.SetPowerZones.as_view(), name='set-zones-pw'),
]
