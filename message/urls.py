from django.urls import path
from views import MessageCreateView


urlpatterns = [
    path('create/', MessageCreateView.as_view(), name='create-message')
]