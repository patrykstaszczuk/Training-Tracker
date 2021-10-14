from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateAccountAPI.as_view(), name='create-account'),
    path('get-token/', views.GetTokenAPI.as_view(), name='get-token')
]
