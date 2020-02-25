from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, CreateView
from clients.models import Client, ApplyClient
from clients.forms import ClientRegisterForm, ApplyClientForm, LoginForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager


class ClientRegister(CreateView):
    model = Client
    form_class = ClientRegisterForm
    template_name = '../templates/clients/sign_up.html'


def Login(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        client = Client.objects.all().filter(email=email, password=password).values()
        if not client:
            messages.info(request, "Email or password is invalid")
            return render(request, 'clients/login.html', context)
        else:

            for i in client:
                id = i['id']
            return HttpResponseRedirect(reverse('clients:apply_client', args=(id,)))
    return render(request, "clients/login.html", context)


def set_login_password(request, id):
    client = get_object_or_404(Client, id=id)
    password = BaseUserManager().make_random_password()
    client.password = password
    client.save()
    # subject = 'Thank you for registering to our site'
    # message =password
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = ['namatullahwahidi@yahoo.com', ]
    # send_mail(subject, message, email_from, recipient_list)
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'account/manager.html', context)


def apply_client(request, id):
    client = get_object_or_404(Client, id=id)
    form = ApplyClientForm(request.POST or None)
    if form.is_valid():
        instance = ApplyClient()
        instance.client = client
        instance.dealTime = form.cleaned_data.get('dealTime')
        instance.credit_purpose = form.cleaned_data.get('credit_purpose')
        instance.credit_amount = form.cleaned_data.get('credit_amount')
        instance.collateral = form.cleaned_data.get('collateral')
        instance.credit_history = form.cleaned_data.get('credit_history')
        instance.finan_perfor = form.cleaned_data.get('finan_perfor')
        instance.save()

        return render(request, '../templates/clients/client_info.html', {'client': instance})

    context = {'form': form,
               'client': client}
    return render(request, 'clients/apply_client.html', context)


def look_to_client(request, id):
    client = get_object_or_404(ApplyClient, id=id)
    return render(request,'clients/client_info.html',{'client':client})


class List_AppliedClients(ListView):
    template_name = 'account/manager.html'
    model = ApplyClient
    context_object_name = 'applied_clients'


class ListClients(ListView):
    template_name = 'account/manager.html'
    model = Client
    context_object_name = 'clients'


def delete_client(request, id):
    article = get_object_or_404(Client, id=id)
    article.delete()
    messages.success(request, "Client  was deleted successfully")
    return redirect("managers:get_client")
