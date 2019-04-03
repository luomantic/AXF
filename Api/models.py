from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    class Meta:
        db_table = 'axf_api_author'
