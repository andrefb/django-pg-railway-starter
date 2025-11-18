from django.urls import path
from .views import account_profile

urlpatterns = [
    path('profile/', account_profile, name='account_profile'),
]
