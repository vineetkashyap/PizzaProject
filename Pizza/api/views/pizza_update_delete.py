from django.shortcuts import render
from api.models import Pizza
from api.serializers import PizzaSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter

# This view will be used to Upadate the Delete the data stored in database

class PizzaUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer  
