from rest_framework import generics
from message.models import Message
from message.serializers import MessageSerializer


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer