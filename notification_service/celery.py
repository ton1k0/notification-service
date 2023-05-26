import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notification_service.settings')

app = Celery('ваш_проект')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
