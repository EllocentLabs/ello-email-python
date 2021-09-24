from django.urls import path
from .views import *

urlpatterns = [
    path('smtp', SmtpApi.as_view()),
    path('sendGrid', SendGridApi.as_view()),
]
