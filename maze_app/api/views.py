from rest_framework.decorators import api_view
from maze_app.models import Customer
from rest_framework.response import Response
from maze_app.api.serializers import CustomerSerializer

# Create your views here.
@api_view()
def customer_details(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)
@api_view()
def customer_list(request, pk):
    customer = Customer.objects.get(pk=pk)
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)