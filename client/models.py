from django.db import models

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=11, unique=True)
    mobile_operator_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=50)
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return self.phone_number
