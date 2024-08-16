from django.urls import path
from .views import *

urlpatterns = [
    path('register/', TestView.as_view(), name='register'),
]