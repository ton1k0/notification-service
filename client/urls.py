from django.urls import path
from client.views import ClientCreateView, ClientUpdateView, ClientDestroyView


urlpatterns = [
    path('add-new-client/', ClientCreateView.as_view(), name='add-new-client'),
    path('<int:pk>/update/', ClientUpdateView.as_view(), name='update-client-information'),
    path('<int:pk>/delete/', ClientDestroyView.as_view(), name='delete-client')
]