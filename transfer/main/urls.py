from django.urls import path

#from . import views
from .views import MainTemplateViev

urlpatterns = [
    path('', MainTemplateViev.as_view(), name='main'),
]
