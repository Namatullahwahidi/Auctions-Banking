from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    pass




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
