from rest_framework import generics

from .models import CoffeeMachine, CoffeePod
from .serializers import CoffeeMachineSerializer, CoffeePodSerializer
from .pagination import ResultsSetPagination


class CoffeeMachineListAPIView(generics.ListAPIView):
    queryset = CoffeeMachine.objects.all()
    serializer_class = CoffeeMachineSerializer
    filterset_fields = ['type', 'water_line_compatible', 'edition']
    pagination_class = ResultsSetPagination


class CoffeePodListAPIView(generics.ListAPIView):
    queryset = CoffeePod.objects.all()
    serializer_class = CoffeePodSerializer
    filterset_fields = ['type', 'flavor', 'size']
    pagination_class = ResultsSetPagination
