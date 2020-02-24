from audioop import reverse

from django.urls import path
from django.conf.urls import url

from clients import views
from clients.views import ListClients,List_AppliedClients,ClientRegister
from clients.models import Client


app_name='clients'
urlpatterns=[
    path('client/',ClientRegister.as_view(model=Client),name='client'),
    path('login/',views.Login,name="login"),
    url(r'^get_client/$',ListClients.as_view(), name='get_client'),
    path('delete_client/<int:id>',views.delete_client,name = "delete_client"),
    path('apply_client/<int:id>',views.apply_client,name = "apply_client"),
    path('look_to_client/<int:id>',views.look_to_client,name = "look_to_client"),
    path('login_password/<int:id>',views.set_login_password,name = "login_password"),
    url(r'^list_applied_clients/$',List_AppliedClients.as_view(), name='list_applied_clients'),

]
