from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from mailing.models import Mailing
from client.models import Client
from message.models import Message
from mailing.serializers import MailingSerializer, MailingStatisticsSerializer, MailingDetailStatisticsSerializer
from datetime import datetime
from rest_framework.response import Response
from celery import shared_task
import requests


@shared_task
def send_message(message_id):
    print(1)
    message = get_object_or_404(Message, id=message_id)

    url = f'https://probe.fbrq.cloud/v1/send/{message.id}'
    headers = {
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTY1NzI2NjEsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Imh0dHBzOi8vdC5tZS90b24xazA0In0.Ih1AevPg2V-nFNDOCUrPkOOpzpjCR9hsoXIcIjOc2Xc'
    }
    data = {
        'id': message.id,
        'phone': message.client.phone_number,
        'text': message.mailing.message_text
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200 or response.json().get('code') == 0:
            # Успешно отправлено
            message.status = 'Sent'
        else:
            # Ошибка отправки
            message.status = 'Error'

        Message.objects.filter(id=message.id).update(status=message.status)

    except requests.exceptions.RequestException:
        # Обработка ошибки при отправке запроса
        message.status = 'Error'
        message.save()

    except requests.exceptions.RequestException:
        # Обработка ошибки при отправке запроса
        message.status = 'Error'
        message.save()



class MailingCreateView(generics.CreateAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    def perform_create(self, serializer):
        # Сохранение рассылки
        mailing = serializer.save()

        current_time = datetime.now()

        if current_time >= mailing.start_datetime and current_time < mailing.end_datetime:
            print(111111)
            clients = Client.objects.filter(
                mobile_operator_code=mailing.mobile_operator_code,
                tag=mailing.tag
            )
            print(clients)


            for client in clients:
                message = Message.objects.create(
                    creation_datetime=datetime.now(),
                    status='Pending',
                    mailing=mailing,
                    client=client
                )
                send_message(message.id)

        return Response({'message': 'Mailing created successfully.'})


class MailingUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': 'Данные о рассылке успешно изменены.'}, status=status.HTTP_200_OK)


class MailingDestroyView(generics.DestroyAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Рассылка успешно удалена'}, status=status.HTTP_204_NO_CONTENT)


class MailingStatisticsView(generics.ListAPIView):
    serializer_class = MailingStatisticsSerializer

    def get_queryset(self):
        queryset = Mailing.objects.annotate(num_messages=Count('message'))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
        for mailing in queryset:
            messages = Message.objects.filter(mailing=mailing)
            statuses = messages.values_list('status', flat=True)
            total_messages = messages.count()
            data.append({
                'mailing_id': mailing.id,
                'statuses': list(statuses),
                'total_messages': total_messages
            })
        return Response(data)


class MailingDetailStatisticsView(generics.RetrieveAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingDetailStatisticsSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)