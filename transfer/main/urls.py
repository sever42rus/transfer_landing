from django.urls import include, path

#from . import views
from .views import *

urlpatterns = [
    path('', Main.as_view(), name='main'),
]
