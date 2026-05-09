from django.contrib import admin
from .models import Customer, Vehicle, Booking,Order,Shipment

admin.site.register(Booking)
admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(Order)
admin.site.register(Shipment)  

