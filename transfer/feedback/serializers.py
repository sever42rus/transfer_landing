from rest_framework import pagination, serializers
from .models import Feedback

class FeedbackCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Feedback
		fields = ('name', 'email', 'telephone', 'message', )