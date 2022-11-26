from rest_framework import serializers
from maze_app.models import Customer

class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    state = serializers.CharField()
    age = serializers.IntegerField()
    active = serializers.BooleanField(default=True)
    
    def create(self, validated_data):
        return Customer.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.state = validated_data.get('state', instance.state)
        instance.age = validated_data.get('age', instance.age)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    
    