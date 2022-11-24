from django.urls import path
from maze_app.views import customer_details

urlpatterns = [
    path('list/', customer_details, name='customer_details') 
]
