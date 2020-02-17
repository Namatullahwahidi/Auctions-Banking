from django import forms
from django.contrib.auth.models import User
from django.forms import ClearableFileInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Client, ApplyClient


class ClientRegisterForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["name", "phone", "message", ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save client'))


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())


class ApplyClientForm(forms.ModelForm):
    class Meta:
        model = ApplyClient
        fields = [
            'dealTime',
            'credit_purpose',
            'credit_amount',
            'collateral',
            'credit_history',
            'finan_perfor',
        ]
