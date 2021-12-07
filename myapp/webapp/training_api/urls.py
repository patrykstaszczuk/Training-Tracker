from django.urls import path
from . import views

app_name = 'training_api'

urlpatterns = [
    path('create/', views.CreateProfileApi.as_view(),
         name='profile-create'),
    path('', views.ProfileApi.as_view(), name='profile'),
]
