from rest_framework import serializers

from .models import Feedback


class FeedbackCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ('name', 'email', 'telephone', 'message', )
