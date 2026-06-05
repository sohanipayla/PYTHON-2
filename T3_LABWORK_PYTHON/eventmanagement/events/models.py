from django.db import models  
from categories.models import Category 

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=100) 
