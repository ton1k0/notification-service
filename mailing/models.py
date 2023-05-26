from django.db import models

class Mailing(models.Model):
    id = models.AutoField(primary_key=True)
    start_datetime = models.DateTimeField()
    message_text = models.TextField()
    mobile_operator_code = models.CharField(max_length=10, blank=True, null=True)
    tag = models.CharField(max_length=50, blank=True, null=True)
    end_datetime = models.DateTimeField()

    def __str__(self):
        return f"Mailing #{self.id}"
