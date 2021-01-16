from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from .models import Plant

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
		