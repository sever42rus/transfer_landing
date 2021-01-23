from django.urls import path

from .views import *

urlpatterns = [
    path('api/recalllist/', RecallListAPI.as_view(), name='recall_list'),
    path('invite/<uuid:invite_id>/',
         RecallInviteAdd.as_view(), name='recall_invite')
]
