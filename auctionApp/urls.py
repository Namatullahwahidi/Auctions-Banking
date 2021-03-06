from django.urls import path
from django.conf.urls import url
from django.urls import path, include
from django.views.generic import UpdateView

from auctionApp.forms import SubscribeForm
from auctionApp.views import managers, clients
from auctionApp.views.clients import ListClients, List_AppliedClients, ClientRegister,SubscribesView
from auctionApp.models import Register, Subscribe
from django.contrib.auth.views import (
    login, logout,
)

urlpatterns = [
    path('', managers.Home, name='home'),
    path('managers/', include(([
           path('manager/', managers.Manager, name='manager'),
           path('bank/', managers.BankRegister, name='bank'),
           url(r'^get_bank/$', managers.getBanks, name='get_bank'),
           url(r'^login/$', login, {'template_name': 'account/login.html'}, name='login'),
           url(r'^logout/$', logout, name='logout'),
       ], 'manager'), namespace='managers')),

    path('clients/', include(([
          path('client/', ClientRegister.as_view(model=Register), name='client'),
          path('login/', clients.Login, name="login"),
          url(r'^get_client/$', ListClients.as_view(), name='get_client'),
          # path('apply/forms/', ApplyForms.as_view(), name='apply_forms'),
          path('delete_client/<int:id>', clients.delete_client, name="delete_client"),
          path('basic/view/<int:id>', clients.BasicView, name="basic_view"),
          path('business/work/view/<int:id>/', clients.BusinessWorkView,
               name="business_work_view"),
          path('credit/line/view/<int:id>/', clients.CreditLineView, name="credit_line_view"),
          path('collateral/view/<int:id>/', clients.CollateralView, name="collateral_view"),
          path('guarantee/view/<int:id>/', clients.GuaranteeView, name="guarantee_view"),
          path('credit/history/view/<int:id>/', clients.CreditHistoryView,
               name="credit_history_view"),
          path('view_a_client/<int:id>/', clients.view_aClient, name="view_a_client"),
          path('accept_client/<int:id>/', clients.accept_client, name="accept_client"),
          path('shared/clients/view/', clients.shared_clients_view, name="shared_clients_view"),
          path('subscribe/view/<int:id>/<int:bankID>/', SubscribesView.as_view(), name="subscribe_view"),
          path('login_password/<int:id>/', clients.set_login_password, name="login_password"),
          url(r'^list_applied_clients/$', List_AppliedClients.as_view(), name='list_applied_clients'),
      ], 'manager'), namespace='clients')),

]
