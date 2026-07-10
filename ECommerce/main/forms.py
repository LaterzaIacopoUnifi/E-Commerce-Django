from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NormalUser

class UserForm(UserCreationForm):
    RULES = (
        ('USER', 'Normal User'),
        ('WORKER', 'Worker'),
        ('MANAGER', 'Manager'),
    )
    first_name = forms.CharField(max_length=20, help_text = "e.g, Iacopo")
    last_name = forms.CharField(max_length=20, help_text="e.g, Laterza")
    rule = forms.CharField(max_length=10)
    birth_date = forms.DateField(label="Data di Nascita",required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    phone_number = forms.CharField(max_length=10)

    class Meta :
        model = NormalUser
        fields = UserCreationForm.Meta.fields + (
            "username" ,
            "first_name" ,
            "last_name" ,
            "email" ,
            "birth_date"
        )