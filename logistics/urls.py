from django.contrib import admin
from django.urls import path,include
from main import views

# 🔥 add this
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('customers/', views.customers, name='customers'),
    path('booking/', views.booking, name='booking'),
    path('feedback/', views.feedback, name='feedback'),
    path('logout/', views.user_logout, name='logout'),
    path('booking/', views.booking, name='booking'),
    path('register/', views.register),
    path('login/', views.user_login),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('orders/', views.orders),
    path('shipments/', views.shipments),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('', include('main.urls')),

]

# 🔥 VERY IMPORTANT
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])