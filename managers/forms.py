# https://stackoverflow.com/questions/38257231/how-can-i-upload-multiple-files-to-a-model-field


from django import forms
from django.contrib.auth.models import User
from django.forms import ClearableFileInput

from .models import Client, ApplyClient
from managers.models import Bank


class ClientRegisterForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["name", "phone", "message", ]


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


class bankRegister(forms.ModelForm):
    documents = forms.FileField(widget=forms.ClearableFileInput(attrs={'id': 'documents', 'required': True,
                                                                       'multiple': True}))

    class Meta:
        model = Bank
        fields = [
            'title',
            'inn',
            'okpo',
            'L_addr',
            'L_addr1',
            'R_person',
            'B_contact',
            'S_contact',
            'currentBalance',
            'documents',
        ]
