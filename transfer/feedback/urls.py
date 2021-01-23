from django.urls import path

from .views import *

urlpatterns = [
    path('api/create/', FeedbackCreate.as_view(), name='feedback_create'),
]
