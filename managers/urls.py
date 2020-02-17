from audioop import reverse

from django.urls import path
from django.conf.urls import url

from managers import views
from managers.views import ListClients,List_AppliedClients,ClientRegister,BankRegister
from managers.models import Client,Bank
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
    path('client/',ClientRegister.as_view(model=Client),name='client'),
    url(r'^get_client/$',ListClients.as_view(), name='get_client'),
    path('delete_client/<int:id>',views.delete_client,name = "delete_client"),
    path('apply_client/<int:id>',views.apply_client,name = "apply_client"),
    url(r'^list_applied_clients/$',List_AppliedClients.as_view(), name='list_applied_clients'),
    path('bank/',BankRegister.as_view(model=Bank),name='bank'),
    url(r'^get_bank/$', views.getBanks, name='get_bank'),
    url(r'^login/$', login,{'template_name':'account/login.html'},  name='login'),
    url(r'^logout/$', logout,name='logout'),

]
