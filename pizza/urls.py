from django.urls import path
from .views import *

urlpatterns = [
    path('menu/', PizzaApiView.as_view()),
    path('orders/', OrdersApiView.as_view()),
]
