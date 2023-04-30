from django import forms
from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','firstname','lastname','gender','email','password','mobile_no','nic','nationality','address')
        labels = {
            'username':'UserName',
            'firstname':'Firstname',
            'lastname':'Lastname',
            'gender':'Gender',
            'email':'E-mail',
            'password':'Password',
            'mobile_no':'Mobile-No',
            'nic':'NIC',
            'nationality':'Nationality',
            'address':'Address'
        }

        widgets = {
            'username': forms.TextInput(attrs ={'class': 'form-control'}),
            'firstname': forms.TextInput(attrs ={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs ={'class': 'form-control'}),
            'gender': forms.TextInput(attrs ={'class': 'form-control'}),
            'email': forms.EmailInput(attrs ={'class': 'form-control'}),
            'password': forms.TextInput(attrs ={'class': 'form-control'}),
            'mobile_no': forms.TextInput(attrs ={'class': 'form-control'}),
            'nic': forms.TextInput(attrs ={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs ={'class': 'form-control'}),
            'address': forms.TextInput(attrs ={'class': 'form-control'}),
        }