from audioop import reverse

from django.urls import path
from django.conf.urls import url

from clients import views
from clients.views import ListClients, List_AppliedClients, ClientRegister
from clients.models import Register

app_name = 'clients'
urlpatterns = [
    path('client/', ClientRegister.as_view(model=Register), name='client'),
    path('login/', views.Login, name="login"),
    url(r'^get_client/$', ListClients.as_view(), name='get_client'),
    # path('apply/forms/', ApplyForms.as_view(), name='apply_forms'),
    path('delete_client/<int:id>', views.delete_client, name="delete_client"),
    path('basic/view/<int:id>', views.BasicView, name="basic_view"),
    path('business/work/view/<int:id>/', views.BusinessWorkView, name="business_work_view"),
    path('credit/line/view/<int:id>/', views.CreditLineView, name="credit_line_view"),
    path('collateral/view/<int:id>/', views.CollateralView, name="collateral_view"),
    path('guarantee/view/<int:id>/', views.GuaranteeView, name="guarantee_view"),
    path('credit/history/view/<int:id>/', views.CreditHistoryView, name="credit_history_view"),
    path('view_a_client/<int:id>/', views.view_aClient, name="view_a_client"),
    path('accept_client/<int:id>/', views.accept_client, name="accept_client"),
    path('shared/clients/view/', views.shared_clients_view, name="shared_clients_view"),
    path('subscribe/view/<int:id>/', views.SubscribesView, name="subscribe_view"),
    path('login_password/<int:id>/', views.set_login_password, name="login_password"),
    url(r'^list_applied_clients/$', List_AppliedClients.as_view(), name='list_applied_clients'),

]
