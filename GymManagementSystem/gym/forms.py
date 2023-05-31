from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Inquiry, Trainer

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ('full_name', 'email', 'message')

class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username') 

class TrainerLoginForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ('username', 'password')
        widgets = {
        'password': forms.PasswordInput(),
    }