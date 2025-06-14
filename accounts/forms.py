
from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm 
from .models import CustomUser
class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    
    class Meta:
        model=CustomUser
        fields=['username','email','phone_number']

class CostomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=['username','email','phone_number','password']