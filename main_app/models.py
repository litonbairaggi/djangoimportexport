from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30, blank=True, default='')
    email = models.EmailField(max_length=30, blank=True, default='')
    birth_date = models.DateField()
    location = models.CharField(max_length=100, blank=True, default='')