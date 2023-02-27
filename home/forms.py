
from cProfile import label
from django import forms 

from .models import login
class loginform(forms.ModelForm):
    class Meta:
        model = login
        fields = '__all__'

        labels = {
           'First_name' : "First_name",
           'Last_name' : "Last_name",
           'Email_address' : "Email_address",
            'Password' : "Password "
        }