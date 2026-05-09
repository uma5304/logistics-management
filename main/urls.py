from django.urls import path
from . import views

urlpatterns = [
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('customers/', views.customers, name='customers'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('orders/', views.orders, name='orders'),
    path('shipments/', views.shipments, name='shipments'),
    path('tracking/', views.tracking, name='tracking'),
    path('booking/', views.booking, name='booking'),
    path('dashboard/customers/', views.admin_customers, name='admin_customers'),
    path('dashboard/orders/', views.admin_orders, name='admin_orders'),
    path('dashboard/vehicles/', views.admin_vehicles, name='admin_vehicles'),
]