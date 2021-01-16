from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from core.models import Plant_table

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

class Plant_tableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plant_table
        fields = ('name', 'price',)