from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .serializers import FeedbackCreateSerializer

# Create your views here.


class FeedbackCreate(CreateAPIView):
    serializer_class = FeedbackCreateSerializer
