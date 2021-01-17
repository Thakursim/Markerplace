from django.urls import path, include
from core.views import CustomerRegistrationView, NurseryRegistrationView
from rest_framework.authtoken.views import obtain_auth_token 
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'plant', views.PlantViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'place_an_order', views.PlaceOrderViewSet, basename='place_an_order') # basename is required
router.register(r'orderplant', views.OrderPlantViewSet) # basename is required

app_name = 'core'

urlpatterns = [
    path('registration/customer/', CustomerRegistrationView.as_view()),
    path('registration/nursery/', NurseryRegistrationView.as_view()),
	path('token-auth/', obtain_auth_token),
	path('', include(router.urls)),
]