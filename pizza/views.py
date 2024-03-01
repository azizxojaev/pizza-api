from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework import status


class PizzaApiView(APIView):
    
    def get(self, request):
        pizzas = Pizza.objects.all()
        serializer = MenuSerializer(instance=pizzas, many=True)
        
        return Response({'pizzas': serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        id = request.data.get('id')
        if Pizza.objects.filter(id=id).exists():
            instance = Pizza.objects.get(id=id)
        else:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.update(instance, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersApiView(APIView):
    
    def get(self, request):
        phone_number = request.GET.get('phone_number')
        orders = Order.objects.filter(phone_number=phone_number)
        serializer = OrdersSerializer(instance=orders, many=True)
        
        return Response({'orders': serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)