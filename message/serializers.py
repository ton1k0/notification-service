from rest_framework import serializers
from message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('__all__')


class MessageInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'date_created', 'status', 'client')