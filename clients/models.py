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

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.client.name
