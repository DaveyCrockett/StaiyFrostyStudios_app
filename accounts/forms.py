from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import widgets
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('role', )

        widgets = {
            'role' : forms.RadioSelect()
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields