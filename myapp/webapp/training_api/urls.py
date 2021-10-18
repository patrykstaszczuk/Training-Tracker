from django.contrib import admin
from django.urls import path
from . import views

app_name = 'training_api'

urlpatterns = [
    path('profile/create', views.CreateProfileApi.as_view(),
         name='profile-create'),
    path('profile', views.RetrieveProfileApi.as_view(), name='profile-retrieve'),
]
