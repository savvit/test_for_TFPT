from django.urls import path
from .views import *

urlpatterns = [
    path('', registration_view, name='reg'),
]