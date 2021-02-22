from django.db import models

# Create your models here.

class Customer(models.Model):
    #id = models.IntegerField(primary_key=True,unique=True,auto_created=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    phone = models.BigIntegerField()
    
    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer,related_name="orders", on_delete=models.CASCADE)
    #id = models.IntegerField(unique=True,primary_key=True,auto_created=True)
    item = models.CharField(max_length=100)
    amount = models.BigIntegerField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item
