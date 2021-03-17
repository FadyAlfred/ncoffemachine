from django.urls import path
from .views import CoffeeMachineListAPIView, CoffeePodListAPIView

urlpatterns = [
    path('machines/', CoffeeMachineListAPIView.as_view(), name='coffee machines'),
    path('pods/', CoffeePodListAPIView.as_view(), name='coffee pods'),
]