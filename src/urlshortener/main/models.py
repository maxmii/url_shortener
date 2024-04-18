from django.db import models


# Create your models here.
class Url(models.Model):
    original_url = models.URLField(max_length=256)
    hash = models.CharField(max_length=10)
    creation_date = models.DateTimeField('creation date')
