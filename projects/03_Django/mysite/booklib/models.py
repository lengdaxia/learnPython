from django.db import models

# Create your models here.
class Book(models.Model):
    """docstring for Book"""
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_house = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
