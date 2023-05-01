from dataclasses import field
from logging import PlaceHolder
from django import forms
from .models import Feedback
from django.forms import ModelForm

class feedbackForms(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('name','mobile_no','email','comments')
        labels = {
            'name':'Name',
            'mobile_no':'Mobile No', 
            'email': 'Email',
            'comments': 'Comments'
        }

        widgets = {
            'name': forms.TextInput(attrs ={'class': 'form-control'}),
            'mobile_no': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs ={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class':'form-control'})
        }