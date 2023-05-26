from django.db import models
from django.utils import timezone

class Mailing(models.Model):
    id = models.AutoField(primary_key=True)
    start_datetime = models.DateTimeField()
    message_text = models.TextField()
    mobile_operator_code = models.CharField(max_length=10, blank=True, null=True)
    tag = models.CharField(max_length=50, blank=True, null=True)
    end_datetime = models.DateTimeField()

    def __str__(self):
        return f"Mailing #{self.id}"

    def save(self, *args, **kwargs):
        if self.start_datetime.tzinfo is not None:
            self.start_datetime = self.start_datetime.replace(tzinfo=None)
        if self.end_datetime.tzinfo is not None:
            self.end_datetime = self.end_datetime.replace(tzinfo=None)
        super().save(*args, **kwargs)


