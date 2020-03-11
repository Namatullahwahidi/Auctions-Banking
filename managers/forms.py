# https://stackoverflow.com/questions/38257231/how-can-i-upload-multiple-files-to-a-model-field

from django import forms
from django.contrib.auth.models import User
from django.db import transaction
from django.forms import ClearableFileInput
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from managers.models import Bank, FeedFile
from clients.models import Register



class BankRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    documents = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'id': 'documents', 'required': True, 'multiple': True}))

    class Meta:
        model = Bank
        fields = [
            'username',
            'email',
            'password',
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save bank'))

# class BankRegisterForm(forms.ModelForm):
#     username = forms.CharField(max_length=100)
#     documents = forms.FileField(widget=forms.ClearableFileInput(
#         attrs={'id': 'documents', 'required': True, 'multiple': True}))
#
#     class Meta:
#         model = Bank
#         fields = ['title', 'inn', 'okpo',
#                   'L_addr', 'L_addr1', 'R_person',
#                   'B_contact', 'S_contact', 'currentBalance', 'documents',
#                   ]
#
#     def clean_username(self):
#         username = self.cleaned_data['username'].lower()
#         r = Bank.objects.filter(username=username)
#         if r.count():
#             raise ValidationError("Username already exists")
#         return username
#
#     @transaction.atomic
#     def save(self, commit=True):
#         bank = super().save(commit=False)
#         bank.save()
#         for f in self.request.FILES.getlist('documents'):
#             user = FeedFile.objects.create(
#                 documents=f,
#                 feed=bank,
#             )
#             user.save()
#         user = Register.objects.create(
#             name=self.cleaned_data['username'],
#             is_bank=True,
#         )
#         return user
#
#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     self.helper = FormHelper()
#     #     self.helper.form_method = 'post'
#     #     self.helper.add_input(Submit('submit', 'Save client'))
