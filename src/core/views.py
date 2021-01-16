from django.shortcuts import render
from rest_framework import viewsets
from rest_auth.registration.views import RegisterView

from rest_framework.permissions import IsAuthenticated
from .models import User, Plant
from .serializers import PlantSerializer, CustomerRegistrationSerializer, NurseryRegistrationSerializer

class CustomerRegistrationView(RegisterView):
    serializer_class = CustomerRegistrationSerializer

class NurseryRegistrationView(RegisterView):
    serializer_class = NurseryRegistrationSerializer
    
class PlantViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    
    def perform_create(self, serializer):
        print(serializer)
        serializer.save(user=self.request.user)
        
    def create(self, request, *args, **kwargs):
        if not request.user.is_nursery:
            message = "Üser is not a nursery."          
            self.permission_denied(request, message)
        return super(PlantViewSet, self).create(request, *args, **kwargs)   
        
    def get_queryset(self):
        if not self.request.user.is_customer:
            message = "You can't view this page."          
            self.permission_denied(self.request, message)
        return super(PlantViewSet, self).get_queryset() 