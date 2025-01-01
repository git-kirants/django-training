from rest_framework import serializers
from .models import Service
from .models import Feedback

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'service_provider', 'title', 'description', 'price', 'availability', 'created_at']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'