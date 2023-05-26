from rest_framework import serializers
from mailing.models import Mailing
from message.serializers import MessageInformationSerializer
from message.models import Message


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = "__all__"


class MailingStatisticsSerializer(serializers.Serializer):
    mailing_id = serializers.IntegerField()
    status = serializers.CharField()
    total_messages = serializers.IntegerField()


class MailingDetailStatisticsSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()

    def get_messages(self, obj):
        messages = obj.message_set.all()
        return MessageInformationSerializer(messages, many=True).data

    class Meta:
        model = Mailing
        fields = ('id', 'start_datetime', 'message_text', 'end_datetime', 'messages')