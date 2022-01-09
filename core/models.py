from django.db import models

# Create your models here.


class Request(models.Model):
    user = models.CharField(max_length=256)
    sales_csv = models.FileField()