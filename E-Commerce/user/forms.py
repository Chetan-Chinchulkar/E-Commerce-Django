from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.modelfields import PhoneNumberField
#from django.core.validators import RegexValidator

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    #phone=forms.PhoneNumberField(blank=True)
    #phone=PhoneNumberField(blank=True)
    

    class Meta:
        model=User
        fields=['username','email','password1','password2']
