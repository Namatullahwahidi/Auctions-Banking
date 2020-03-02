from django.db import models
from django.utils import timezone
from managers.models import Bank


class Client(models.Model):
    name = models.CharField(max_length=42)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    password = models.CharField(max_length=128, default=None, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    state = models.BooleanField(default=0)

    class Meta:
        ordering = ['-created_date']

    def get_absolute_url(self):
        return u'/'
        # return u'/manager/%d' % self.id

    def __str__(self):
        return self.name



class BasicInformation(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
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


class Business(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    kind_activity = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    employee_num = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']


class Works(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    kind_activity = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    certificate = models.FileField(upload_to="media/clients", default='/media/index.jpeg', blank=True)

    class Meta:
        ordering = ['-id']


class Credit_line(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    proposed_loan = models.CharField(max_length=100)
    credit_amount = models.CharField(max_length=100)
    period = models.DateTimeField()
    goal = models.CharField(max_length=100)
    contribution_amount = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)

    class Meta:
        ordering = ['-id']


class Collateral(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    market_value = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']


class Guarantee(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    No = models.PositiveIntegerField()
    applicant = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    income = models.CharField(max_length=100)
    market_value = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']


class Credit_History(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    bank = models.CharField(max_length=100)
    receiving_date = models.DateTimeField()
    return_date = models.DateTimeField()
    maturity_date = models.DateTimeField()
    rate = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)
    currency_unit = models.CharField(max_length=10)

    class Meta:
        ordering = ['-id']


class AcceptClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    credit_line = models.ForeignKey(Credit_line, on_delete=models.CASCADE)
    collateral = models.ForeignKey(Collateral, on_delete=models.CASCADE)
    credit_history = models.ForeignKey(Credit_History, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField(default=timezone.now)
    start_rate = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)


class Subscribe(models.Model):
    client = models.ForeignKey(AcceptClient, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, default=0)
