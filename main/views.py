import uuid
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from .models import Booking
from django.contrib import messages 
from .models import Customer
from .models import Vehicle
from .models import Order, Shipment
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required(login_url='/login/')
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')
def contact(request):
    return render(request, 'contact.html')    

def booking(request):
    vehicles = Vehicle.objects.all()

    if request.method == "POST":
        # customer
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')

        # order
        pickup = request.POST.get('pickup')
        delivery = request.POST.get('delivery')
        goods = request.POST.get('goods')
        weight = request.POST.get('weight')

        # AUTO BOOKING ID
        booking_id = "ORD" + str(uuid.uuid4())[:8]

        customer = Customer.objects.create(
            booking_id=booking_id,
            name=name,
            phone=phone,
            city=city
        )

        order = Order.objects.create(
            booking_id=booking_id,
            customer=customer,
            pickup=pickup,
            delivery=delivery,
            goods=goods,
            weight=weight,
        )

        Shipment.objects.create(order=order)

        # ✅ SUCCESS PAGE (INSIDE IF)
        return render(request, 'success.html', {'id': booking_id})

    # ✅ GET REQUEST
    return render(request, 'booking.html', {'vehicles': vehicles})
# REGISTER
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('/register/')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully")
        return redirect('/login/')

    return render(request, 'register.html')


# LOGIN
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')   # dashboard/home
        else:
            messages.error(request, "Invalid login")

    return render(request, 'login.html')


# LOGOUT
def user_logout(request):
    logout(request)
    return redirect('/login/')


def customers(request):
    data = Customer.objects.all()
    return render(request, 'customers.html', {'data': data})



def vehicles(request):
    data = Vehicle.objects.all()
    return render(request, 'vehicles.html', {'data': data})

def orders(request):
    data = Order.objects.all()
    return render(request, 'orders.html', {'data': data})


def shipments(request):
    data = None

    if request.method == "POST":
        booking_id = request.POST.get('booking_id')

        try:
            data = Order.objects.get(booking_id=booking_id)
        except:
            data = None

    return render(request, 'shipments.html', {'data': data})
def tracking(request):
    data = None

    if request.method == "POST":
        booking_id = request.POST.get('booking_id')

        try:
            data = Order.objects.get(booking_id=booking_id)
        except:
            data = None

    return render(request, 'tracking.html', {'data': data})

def feedback(request):
    if request.method == "POST":
        booking_id = request.POST.get('booking_id')
        feedback_text = request.POST.get('feedback')

        customer = Customer.objects.get(booking_id=booking_id)
        customer.feedback = feedback_text
        customer.save()

        return redirect('home')    


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid Login'})

    return render(request, 'admin_login.html')

def admin_dashboard(request):
    customers = Customer.objects.all()
    vehicles = Vehicle.objects.all()
    orders=Order.objects.all()
    return render(request, 'admin_dashboard.html', {
        'customers': customers,
        'vehicles': vehicles,
        'orders':orders
    })

def admin_customers(request):
    data = Customer.objects.all()
    return render(request, 'admin_customers.html', {'data': data})


def admin_orders(request):
    data = Order.objects.all()
    return render(request, 'admin_orders.html', {'data': data})


def admin_vehicles(request):
    vehicles = Vehicle.objects.all()
    error = None

    if request.method == "POST":
        vehicle_id = request.POST.get('vehicle_id')
        vehicle_type = request.POST.get('type')
        capacity = request.POST.get('capacity')

        # 🔥 duplicate check
        if Vehicle.objects.filter(vehicle_id=vehicle_id).exists():
            error = "Vehicle ID already exists!"
        else:
            Vehicle.objects.create(
                vehicle_id=vehicle_id,
                vehicle_type=vehicle_type,
                capacity=capacity
            )

    return render(request, 'admin_vehicles.html', {
        'vehicles': vehicles,
        'error': error
    })