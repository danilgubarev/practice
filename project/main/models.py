from django.db import models

# Create your models here.


class Vacansies(models.Model):
    company = models.CharField(max_length=255)
    salary = models.IntegerField()
    email = models.CharField(max_length=255)
    conditions = models.CharField(max_length=255)
    