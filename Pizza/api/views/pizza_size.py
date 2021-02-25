from django.shortcuts import render
from api.models import PizzaSize
from api.serializers import PizzaSizeSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.filters import SearchFilter

# This view will be used to add the size of  pizza and will be stored  in database
class PizzaSize(CreateAPIView):
    queryset = PizzaSize.objects.all()
    serializer_class = PizzaSizeSerializer  
