from django.shortcuts import render
from api.models import Pizza,PizzaSize
from api.serializers import PizzaSerializerList
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

"""
 This veiw will be used to list all pizza  and if you want to search according to pizza size,pizza type, pizza toppings this will also give the exact result
 """
class PizzaList(ListAPIView):
    queryset = Pizza.objects.all()   
    serializer_class = PizzaSerializerList
    filter_backends = [SearchFilter]
    search_fields = ['pizza_type','pizza_topp','pizza_size__pizza_size']