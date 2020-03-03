from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser


class Profile(models.Model):
    CLIENTS = 1
    DOCTORS = 2
    ADMIN = 3
    ROLE_CHOICES = (
        (CLIENTS, 'Clients'),
        (DOCTORS, 'Doctors'),
        (ADMIN, 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, default=CLIENTS)
# class User(AbstractUser):
#     USER_TYPE_CHOICES = (
#         (1, 'admin'),
#         (2, 'bank'),
#         (3, 'client'),
#     )
#
#     user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
# class User(AbstractUser):
#     is_student = models.BooleanField('student status', default=False)
#     is_teacher = models.BooleanField('teacher status', default=False)

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
