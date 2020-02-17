from audioop import reverse

from django.urls import path
from django.conf.urls import url

from managers import views
from managers.views import BankRegister
from managers.models import Bank
from django.contrib.auth.views import (
    login,logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)

app_name='managers'
urlpatterns=[
    path('',views.Home,name='home'),
    path('manager/',views.Manager,name='manager'),
    path('bank/',BankRegister.as_view(model=Bank),name='bank'),
    url(r'^get_bank/$', views.getBanks, name='get_bank'),
    url(r'^login/$', login,{'template_name':'account/login.html'},  name='login'),
    url(r'^logout/$', logout,name='logout'),

]
