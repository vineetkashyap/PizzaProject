from django.urls import path
from api.views.pizza_list import PizzaList
from api.views.pizza_create import PizzaCreate
from api.views.pizza_update_delete import PizzaUpdateDelete
from api.views.pizza_size import PizzaSize
urlpatterns = [
    
    path('list/',PizzaList.as_view()),
    path('create/',PizzaCreate.as_view()),
    path('deleteorupdate/<int:pk>/',PizzaUpdateDelete.as_view()),
    path('size/',PizzaSize.as_view()),
]
