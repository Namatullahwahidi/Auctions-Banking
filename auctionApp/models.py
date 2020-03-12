from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Register(models.Model):
    username = models.CharField(max_length=42)
    phone = models.CharField(max_length=15, default="")
    email = models.EmailField(max_length=100)
    message = models.TextField(default="")
    password = models.CharField(max_length=128, default=None, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    is_client = models.BooleanField(default=False)
    is_bank = models.BooleanField(default=False)
    state=models.BooleanField(default=False)
    class Meta:
        ordering = ['-created_date']

    def get_absolute_url(self):
        return u'/'
        # return u'/manager/%d' % self.id

    def __str__(self):
        return self.username


class Bank(models.Model):
    title = models.CharField(max_length=100)
    inn = models.CharField(max_length=100)
    okpo = models.CharField(max_length=100)
    L_addr = models.CharField(max_length=150)
    L_addr1 = models.CharField(max_length=150)
    R_person = models.CharField(max_length=100)
    B_contact = models.CharField(max_length=150)
    S_contact = models.CharField(max_length=150)
    currentBalance = models.DecimalField(max_digits=20, decimal_places=4, blank=False, null=False, default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return u'/get_bank'


class FeedFile(models.Model):
    documents = models.FileField(upload_to="media", default='/media/index.jpeg', blank=True)
    feed = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='documents')


class BasicInformation(models.Model):
    client = models.OneToOneField(Register, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=100)
    spouse_name = models.CharField(max_length=100)
    dependant = models.CharField(max_length=100)
    birth_date = models.CharField(max_length=100)
    birth_palce = models.CharField(max_length=100)
    passport_no = models.CharField(max_length=100)
    issued_by = models.CharField(max_length=100)
    issued_date = models.CharField(max_length=100)
    register_place = models.CharField(max_length=100)
    residential_add = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    inn = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100)
    education = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.applicant_name;


class Business(models.Model):
    client = models.OneToOneField(Register, on_delete=models.CASCADE)
    kind_activity = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    employee_num = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.kind_activity


class Works(models.Model):
    client = models.OneToOneField(Register, on_delete=models.CASCADE)
    kind_activity = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    certificate = models.FileField(upload_to="media/clients", default='/media/index.jpeg', blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.kind_activity


class Credit_line(models.Model):
    client = models.OneToOneField(Register, on_delete=models.CASCADE)
    proposed_loan = models.CharField(max_length=100)
    credit_amount = models.CharField(max_length=100)
    period = models.DateTimeField()
    goal = models.CharField(max_length=100)
    contribution_amount = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.contribution_amount


class Collateral(models.Model):
    client = models.OneToOneField(Register, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    market_value = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.description


class Guarantee(models.Model):
    client = models.OneToOneField(Register, on_delete=models.CASCADE)
    No = models.PositiveIntegerField()
    applicant = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    income = models.CharField(max_length=100)
    market_value = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.applicant


class Credit_History(models.Model):
    client = models.OneToOneField(Register, on_delete=models.CASCADE)
    bank = models.CharField(max_length=100)
    receiving_date = models.DateTimeField()
    return_date = models.DateTimeField()
    maturity_date = models.DateTimeField()
    rate = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)
    currency_unit = models.CharField(max_length=10)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.bank


class AcceptClient(models.Model):
    client = models.ForeignKey(Register, on_delete=models.CASCADE)
    credit_line = models.ForeignKey(Credit_line, on_delete=models.CASCADE)
    collateral = models.ForeignKey(Collateral, on_delete=models.CASCADE)
    credit_history = models.ForeignKey(Credit_History, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField(default=timezone.now)
    start_rate = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)

    def __str__(self):
        return self.client.username


class Subscribe(models.Model):
    accept_client = models.ForeignKey(AcceptClient, on_delete=models.CASCADE)
    bank = models.ForeignKey(Register, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)

    # number_choice = [(i,i) for i in range(accept_client.credit_line.contribution_amount,accept_client.start_rate)]

    # num_of_adults = models.DecimalField(default=0, choices=number_choice,null=True)

    def __str__(self):
        return self.accept_client.client
