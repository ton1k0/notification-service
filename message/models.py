from django.db import models
from client.models import Client
from mailing.models import Mailing


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    creation_datetime = models.DateTimeField()
    status = models.CharField(max_length=50)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"Message #{self.id}"

