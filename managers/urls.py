from audioop import reverse

from django.urls import path
from django.conf.urls import url

from managers import views
from managers.views import BankRegister,Shared_client_list
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
    path('bank/',views.BankRegister,name='bank'),
    url(r'^get_bank/$', views.getBanks, name='get_bank'),
    path('shared_client/<int:id>', views.shared_client, name="shared_client"),
    url(r'^shared/client/list/$', Shared_client_list.as_view(), name='shared_client_list'),
    url(r'^login/$', login,{'template_name':'account/login.html'},  name='login'),
    url(r'^logout/$', logout,name='logout'),

]
