# serializers.py in your chatbot app

from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'text', 'created_at', 'is_user_message', 'session']
        read_only_fields = ['id', 'created_at', 'is_user_message', 'session']

    def create(self, validated_data):
        # Custom create method to handle saving the message instance
        # Assuming the session is retrieved from the `validated_data` or the context
        return Message.objects.create(**validated_data)
