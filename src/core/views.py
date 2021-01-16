from django.shortcuts import render
from rest_framework import viewsets
from rest_auth.registration.views import RegisterView

from rest_framework.permissions import IsAuthenticated
from core.serializers import (
    CustomerRegistrationSerializer, NurseryRegistrationSerializer
    )
from .models import User, Plant_table
from .serializers import Plant_tableSerializer

class CustomerRegistrationView(RegisterView):
    serializer_class = CustomerRegistrationSerializer


class NurseryRegistrationView(RegisterView):
    serializer_class = NurseryRegistrationSerializer
	
class Plant_tableViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Plant_table.objects.all()
    serializer_class = Plant_tableSerializer