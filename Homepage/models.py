from django.db import models

# Create your models here.

class DataSetText(models.Model):
    text = models.TextField(max_length=1000)
    rating = models.IntegerField(default=0)
