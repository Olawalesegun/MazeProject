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