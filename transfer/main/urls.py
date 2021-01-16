from django.urls import path, include
#from . import views
from .views import *

urlpatterns = [
    path('', Main.as_view(), name='main'),
]