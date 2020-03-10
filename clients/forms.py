from django import forms
from django.contrib.auth.models import User
from django.db import transaction
from django.forms import ClearableFileInput
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from .models import Register
from clients.models import BasicInformation, Business, AcceptClient, \
    Works, Credit_line, Collateral, Guarantee, Credit_History, Subscribe


# class ClientRegisterForm(forms.ModelForm):
#     # password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = Register
#         fields = ["name", "phone", 'email', "message"]
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Save client'))

class ClientRegisterForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Register
        fields = ["name", "phone", 'email', "message"]

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    @transaction.atomic
    def save(self, commit=True):
        user = Register.objects.create(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            phone=self.cleaned_data['phone'],
            message=self.cleaned_data['message'],
            is_client=True,
        )
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save client'))



class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())


class BasicInformationForm(forms.ModelForm):
    class Meta:
        model = BasicInformation
        fields = [
            'applicant_name',
            'spouse_name',
            'dependant',
            'birth_date',
            'birth_palce',
            'passport_no',
            'issued_by',
            'issued_date',
            'register_place',
            'residential_add',
            'region',
            'inn',
            'contacts',
            'education'
        ]


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = [
            'kind_activity',
            'experience',
            'employee_num',
            'address',
        ]


class WorksForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = [
            'kind_activity',
            'experience',
            'address',
            'certificate',
        ]


class Credit_LineForm(forms.ModelForm):
    class Meta:
        model = Credit_line
        fields = [
            'proposed_loan',
            'credit_amount',
            'period',
            'goal',
            'contribution_amount',
        ]


class CollateralForm(forms.ModelForm):
    class Meta:
        model = Collateral
        fields = [
            'description',
            'owner',
            'location',
            'market_value',
        ]


class GuaranteeForm(forms.ModelForm):
    class Meta:
        model = Guarantee
        fields = [
            'No',
            'applicant',
            'address',
            'income',
            'market_value',
        ]


class Credit_HistoryForm(forms.ModelForm):
    class Meta:
        model = Credit_History
        fields = [
            'bank',
            'receiving_date',
            'return_date',
            'maturity_date',
            'rate',
            'currency_unit',

        ]


class AcceptClientForm(forms.ModelForm):
    class Meta:
        model = AcceptClient
        fields = [
            'start_date',
            'expire_date',
            'start_rate',
        ]


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = []
