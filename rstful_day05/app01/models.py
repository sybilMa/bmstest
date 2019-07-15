from django.db import models

# Create your models here.
class Publish(models.Model):
    name=models.CharField(max_length=32)
    city=models.CharField(max_length=64)