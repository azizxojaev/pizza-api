from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    weight = models.FloatField()
    calories = models.PositiveIntegerField()
    size = models.CharField(max_length=30)
    
    
class Order(models.Model):
    phone_number = models.CharField(max_length=30)
    products = models.ManyToManyField(Pizza, related_name='pizzas', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    
    class Meta:
        ordering = ['-created']