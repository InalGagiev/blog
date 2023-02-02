from django.urls import path
from .views import *

urlpatterns = [
    path('', main_registration, name='main_registration'),
    path('profile', profile_view, name='reg_profile')
]