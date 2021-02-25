from rest_framework import serializers
from .models import Pizza,PizzaSize

#  This serailizer has been used to create a pizza size and that will be stored in the database
class PizzaSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaSize
        fields = ['id','pizza_size']

# This serializer class  has been used to store the data regarding to pizza in the database
class PizzaSerializer(serializers.ModelSerializer):
    size = serializers.ReadOnlyField(source='pizza_size.pizza_size')
    class Meta:
        model = Pizza
        fields = ['id','pizza_type','pizza_size','size','pizza_topp']

# This serializer class has been used to show the list of the pizza
class PizzaSerializerList(serializers.ModelSerializer):
    size = serializers.ReadOnlyField(source='pizza_size.pizza_size')
    class Meta:
        model = Pizza
        fields = ['id','pizza_type','size','pizza_topp']
        