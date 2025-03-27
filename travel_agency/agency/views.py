from django.shortcuts import render, redirect
from .models import Tour, Customer, Booking
from .forms import CustomerForm, BookingForm
import os

# View to list available tours
def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'agency/tour_list.html', {'tours': tours})

# View to register a customer
def customer_register(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tour_list')
    else:
        form = CustomerForm()
    return render(request, 'agency/customer_register.html', {'form': form})

# View to make a booking
def make_booking(request, tour_id):
    tour = Tour.objects.get(id=tour_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tour_list')
    else:
        form = BookingForm(initial={'tour': tour})
    return render(request, 'agency/make_booking.html', {'form': form, 'tour': tour})

def home(request):
    return render(request, 'home.html')

def home(request):
    return render(request, os.path.join('agency', 'home.html'))
