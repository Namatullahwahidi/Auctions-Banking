from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=42)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    password = models.CharField(max_length=128, default=None, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def get_absolute_url(self):
        return u'/'
        # return u'/manager/%d' % self.id

    def __str__(self):
        return self.name


class ApplyClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dealTime = models.DateTimeField(default=timezone.now)
    credit_purpose = models.CharField(max_length=100)
    credit_amount = models.CharField(max_length=100)
    collateral = models.CharField(max_length=200)
    credit_history = models.CharField(max_length=200)
    finan_perfor = models.CharField(max_length=100)
    created_date = models.DateTimeField(
        default=timezone.now)
    state = models.BooleanField(default=0)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.client.name


class BasicInformation(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    applicant_name=models.CharField(max_length=100)
    spouse_name=models.CharField(max_length=100)
    dependant=models.CharField(max_length=100)
    birth_date=models.CharField(max_length=100)
    birth_palce=models.CharField(max_length=100)
    passport_no=models.CharField(max_length=100)
    issued_by=models.CharField(max_length=100)
    issued_date=models.CharField(max_length=100)
    register_place=models.CharField(max_length=100)
    residential_add=models.CharField(max_length=100)
    region=models.CharField(max_length=100)
    inn=models.CharField(max_length=100)
    contacts=models.CharField(max_length=100)
    education=models.CharField(max_length=100)

