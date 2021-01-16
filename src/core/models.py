from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_customer = models.BooleanField(default=False)
  is_nursery = models.BooleanField(default=False)
  
class Plant_table(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    # image = models.ImageField(upload_to=)
    
    def __str__(self):
        return self.name