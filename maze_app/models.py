from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    age = models.IntegerField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
