from django.db.models import Count
from rest_framework import generics, status
from rest_framework.response import Response
from mailing.models import Mailing
from mailing.serializers import MailingSerializer, MailingStatisticsSerializer, MailingDetailStatisticsSerializer


class MailingCreateView(generics.CreateAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


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
        return Response({'message': 'Рассылка успешно удален'}, status=status.HTTP_204_NO_CONTENT)


class MailingStatisticsView(generics.ListAPIView):
    serializer_class = MailingStatisticsSerializer

    def get_queryset(self):
        queryset = Mailing.objects.annotate(num_messages=Count('message'))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
        for mailing in queryset:
            data.append({
                'mailing_id': mailing.id,
                'status': mailing.message.status,
                'total_messages': mailing.num_messages
            })
        return Response(data, status=status.HTTP_200_OK)


class MailingDetailStatisticsView(generics.RetrieveAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingDetailStatisticsSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)