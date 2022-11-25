from rest_framework import serializers
from maze_app.models import Customer

class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField()
    state = serializers.CharField()
    age = serializers.IntegerField()
    active = serializers.BooleanField(default=True)