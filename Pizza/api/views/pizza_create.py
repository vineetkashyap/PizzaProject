from django.shortcuts import render
from api.models import Pizza,PizzaSize
from api.serializers import PizzaSerializer
from rest_framework.generics import CreateAPIView

# this view will create a new pizza
class PizzaCreate(CreateAPIView):
       queryset = Pizza.objects.all()
       serializer_class = PizzaSerializer  