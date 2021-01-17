from django.contrib import admin
from .models import User, Plant, Cart, Order, OrderPlant
# Register your models here.

admin.site.register(User)
admin.site.register(Plant)
admin.site.register(Cart)
admin.site.register(OrderPlant)
admin.site.register(Order)