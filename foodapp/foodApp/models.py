import email
from unicodedata import name
from django.db import models

# Create your models here.

class RestaurantServiceRegistration(models.Model):
    emailId = models.EmailField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    


