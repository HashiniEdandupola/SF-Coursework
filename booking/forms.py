from django import forms
from .models import Booking_detail

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking_detail
        fields = ('email','name','checking_date','checkout_date','room','mobile_no')
        labels = {
            'email':'Email',
            'name':'Name',
            'checking_date':'Checking date',
            'checkout_date':'Checkout-date',
            'room':'Room',
            'mobile_no':'Mobile No',
            'mobile_no':'Mobile-No',
        }

        widgets = {
            'email': forms.EmailInput(attrs ={'class': 'form-control'}),
            'name': forms.TextInput(attrs ={'class': 'form-control'}),
            'checking_date': forms.TextInput(attrs ={'class': 'form-control'}),
            'checkout_date': forms.TextInput(attrs ={'class': 'form-control'}),
            'room': forms.TextInput(attrs ={'class': 'form-control'}),
            'mobile_no': forms.TextInput(attrs ={'class': 'form-control'})
        }

        