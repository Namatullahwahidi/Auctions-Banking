from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    pass


class Client(models.Model):
    name = models.CharField(max_length=42)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    class Meta:
        ordering = ['-created_date']

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

    def __str__(self):
        return self.client


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


class FeedFile(models.Model):
    documents = models.FileField(upload_to="media", default='/media/index.jpeg', blank=True)
    feed = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='files')
