from django import forms
from .models import Customer, Booking

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'tour', 'number_of_people']
        widgets = {
            'tour': forms.HiddenInput(),
        }
