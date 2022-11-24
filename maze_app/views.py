from django.shortcuts import render
from maze_app.models import Customer
from django.http import JsonResponse

# Create your views here.
def customer_details(request):
    customer = Customer.objects.all()
    data = {
        'customer': list(customer.values())
    }
    return JsonResponse(data)

def customer_list(request, pk):
    customer = Customer.objects.get(pk=pk)
    data = {
        'name': customer.name,
        'state': customer.state,
        'age': customer.age,
        'active': customer.active 
    }
    return JsonResponse(data)