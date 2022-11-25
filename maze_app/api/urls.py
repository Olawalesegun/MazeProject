from django.urls import path
from maze_app.api.views import customer_details, customer_list

urlpatterns = [
    path('list/', customer_details, name='customer-details'), 
    path('<int:pk>', customer_list, name='customer-list'),
]
