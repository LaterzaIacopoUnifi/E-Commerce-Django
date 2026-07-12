from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from .models import NormalUser

class UserForm(UserCreationForm):
    ROLES = (
        ('NormalUser', 'Normal User'),
        ('WORKER', 'Worker'),
        ('MANAGER', 'Manager'),
    )
    first_name = forms.CharField(max_length=20, help_text = "e.g, Iacopo")
    last_name = forms.CharField(max_length=20, help_text="e.g, Laterza")
    role = forms.ChoiceField(choices=ROLES,widget=forms.RadioSelect,required=True,label="Ruolo")
    birth_date = forms.DateField(label="Data di Nascita",required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    phone_number = forms.CharField(max_length=10)


    def save(self, commit=True):
        user: NormalUser = super().save(commit=False)

        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.birth_date = self.cleaned_data.get('birth_date')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.role = self.cleaned_data.get('role')

        if commit:
            user.save()

        role = self.cleaned_data.get('role')
        if role:
            group = Group.objects.get(name=role)
            user.groups.add(group)
        return user

    class Meta :
        model = NormalUser
        fields = UserCreationForm.Meta.fields + (
            "username" ,
            "first_name" ,
            "last_name" ,
            "email" ,
            "birth_date",
            "role",
        )