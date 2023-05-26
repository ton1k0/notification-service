from rest_framework import generics, status
from client.models import Client
from client.serilalizers import ClientSerializer
from rest_framework.response import Response


class ClientCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': 'Данные о клиенте успешно изменены.'}, status=status.HTTP_200_OK)


class ClientDestroyView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Клиент успешно удален'}, status=status.HTTP_204_NO_CONTENT)