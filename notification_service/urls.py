from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', include('client.urls')),
    path('mailing/', include('mailing.urls')),
    path('message/', include('message.urls')),
]
