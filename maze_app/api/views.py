from rest_framework.decorators import api_view
from maze_app.models import Customer
from rest_framework.response import Response
from maze_app.api.serializers import CustomerSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def customer_details(request):
    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
@api_view(['GET', 'PUT', 'DELETE'])
def customer_list(request, pk):
    if request.method == 'GET':
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    if request.method == 'PUT':
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method == 'DELETE':
        customer = Customer.objects.get(pk=pk)
        customer.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
            
        