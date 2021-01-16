from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from .models import Plant, Cart, Order

class CustomerRegistrationSerializer(RegisterSerializer):
    def save(self, request):
        user = super(CustomerRegistrationSerializer, self).save(request)
        user.is_customer = True
        user.save()
        return user

class NurseryRegistrationSerializer(RegisterSerializer):
    def save(self, request):
        user = super(NurseryRegistrationSerializer, self).save(request)
        user.is_nursery = True
        user.save()
        return user

class PlantSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Plant
        fields = ('id', 'name', 'price', 'image',)
		
class CartSerializer(serializers.ModelSerializer):
	# Modelserializer is use to save the plant_id foreignkey.
    id = serializers.IntegerField(read_only=True)
    class Meta:
         model = Cart
         fields = ('id', 'plant',)		

# class OrderSerializer(serializers.ModelSerializers):
    # id = serializers.IntergerField(read_only=True)
    # class Meta:
        # model = Order
        # fields = ('id', 'plants',)		