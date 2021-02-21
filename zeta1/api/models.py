from django.db import models

# Create your models here.


class Quotes(models.Model):
    quote=models.CharField(max_length=100)
    author= models.CharField(max_length=50)