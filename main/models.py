import uuid
from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=200)
    service = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# CUSTOMER
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    booking_id = models.CharField(max_length=20, unique=True)
    feedback = models.TextField(blank=True, null=True)  
    
    def __str__(self):
        return self.name


# VEHICLE
class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=20, unique=True,default="Unknown")
    vehicle_type = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.number


# ORDER
class Order(models.Model):
    booking_id = models.CharField(max_length=50, unique=True,default="Unknown")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pickup = models.CharField(max_length=200)
    delivery = models.CharField(max_length=200)
    goods = models.CharField(max_length=100)
    weight = models.IntegerField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)

STATUS_CHOICES = [
    ("confirmed", "Order Confirmed"),
    ("assigned", "Vehicle Assigned"),
    ("picked", "Goods Picked Up"),
    ("transit", "In Transit"),
    ("delivered", "Delivered"),
]

class Shipment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="confirmed")    