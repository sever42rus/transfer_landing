from rest_framework import serializers

from .models import Recall


class RecallListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recall
        fields = '__all__'
        depth = 1
