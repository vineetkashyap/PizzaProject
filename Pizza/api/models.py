from django.db import models

# Create your models here

#  Here I have used many to one relation between PizzaSize and Pizza so that user can add pizza size according to his/her will 

class PizzaSize(models.Model):
     pizza_size = models.CharField(max_length=40)
     def __str__(self):
         return self.pizza_size

class Pizza(models.Model):
    PIZZA_TYPE =[
        ('Regular','Regular'),
        ('Square','Square'),
    ]
    pizza_type = models.CharField(max_length=50, choices=   PIZZA_TYPE)
    pizza_size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE,related_name='size')
    pizza_topp = models.CharField(max_length=50)
    def __str__(self):
        return self.pizza_size
   
    