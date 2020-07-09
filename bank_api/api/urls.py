from django.urls import path
from .views import *

urlpatterns = [
    path('',BankDetails.as_view()),
]
