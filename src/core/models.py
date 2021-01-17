from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_customer = models.BooleanField(default=False)
  is_nursery = models.BooleanField(default=False)
  
class Plant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/')
    
    def __str__(self):
        return self.name
        
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)  
    
    def __str__(self):
        return str(self.plant)
        
class Order(models.Model):
    plants = models.ManyToManyField(Plant, through='OrderPlant')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "Order by user id -" + str(user.id)
		
class OrderPlant(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    