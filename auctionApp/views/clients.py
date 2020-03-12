from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, CreateView
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist

from auctionApp.forms import ClientRegisterForm, LoginForm
from auctionApp.forms import BasicInformationForm, BusinessForm, AcceptClientForm, \
    WorksForm, Credit_LineForm, CollateralForm, GuaranteeForm, Credit_HistoryForm, SubscribeForm
from auctionApp.models import BasicInformation, Business, Works, Credit_line, \
    Collateral, Guarantee, Credit_History, AcceptClient, Subscribe
from auctionApp.models import Register


class ClientRegister(CreateView):
    model = Register
    form_class = ClientRegisterForm
    template_name = '../templates/clients/sign_up.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)


def Login(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        # user = Register.objects.all().filter(email=email, password=password)
        try:
            user = Register.objects.get(email=email, password=password)
        except ObjectDoesNotExist:
            messages.info(request, "Email or password is invalid")
            return render(request, 'clients/login.html', context)
        else:
            if user.is_client:
                return HttpResponseRedirect(reverse('clients:basic_view', args=(user.id,)))
            elif user.is_bank:
                accepted_clients = AcceptClient.objects.all()
                context = {
                    'accepted_clients': accepted_clients,
                    "bank": user
                }
                return render(request, "clients/shared_clients.html", context)
    return render(request, "clients/login.html", context)


def BasicView(request, id):
    client = get_object_or_404(Register, id=id)
    basic_form = BasicInformationForm(request.POST or None)
    if basic_form.is_valid():
        instance = basic_form.save(commit=False)
        instance.client = client
        id = client.id
        instance.save()
        return HttpResponseRedirect(reverse('clients:business_work_view', args=(id,)))
    context = {'form': basic_form}
    return render(request, 'clients/client_forms.html', context)


def BusinessWorkView(request, id):
    client = get_object_or_404(Register, id=id)
    form = BusinessForm(request.POST or None)
    form1 = WorksForm(request.POST or None, request.FILES)
    if form.is_valid() and form1.is_valid():
        instance = form.save(commit=False)
        instance.client = client
        id = client.id
        instance.save()
        instance1 = form1.save(commit=False)
        instance1.client = client
        instance1.save()
        return HttpResponseRedirect(reverse('clients:credit_line_view', args=(id,)))
    context = {'form': form, 'form1': form1}
    return render(request, 'clients/client_forms.html', context)


def CreditLineView(request, id):
    client = get_object_or_404(Register, id=id)
    form = Credit_LineForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.client = client
        id = client.id
        instance.save()
        return HttpResponseRedirect(reverse('clients:collateral_view', args=(id,)))
    context = {'form': form, }
    return render(request, 'clients/client_forms.html', context)


def CollateralView(request, id):
    client = get_object_or_404(Register, id=id)
    form = CollateralForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.client = client
        id = client.id
        instance.save()
        return HttpResponseRedirect(reverse('clients:guarantee_view', args=(id,)))
    context = {'form': form, }
    return render(request, 'clients/client_forms.html', context)


def GuaranteeView(request, id):
    client = get_object_or_404(Register, id=id)
    form = GuaranteeForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.client = client
        id = client.id
        instance.save()
        return HttpResponseRedirect(reverse('clients:credit_history_view', args=(id,)))
    context = {'form': form, }
    return render(request, 'clients/client_forms.html', context)


def CreditHistoryView(request, id):
    client = get_object_or_404(Register, id=id)
    form = Credit_HistoryForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.client = client
        id = client.id
        instance.save()
        return redirect("/")
    context = {'form': form, }
    return render(request, 'clients/client_forms.html', context)


def set_login_password(request, id):
    client = get_object_or_404(Register, id=id)
    password = BaseUserManager().make_random_password()
    client.password = password
    client.save()
    print(password)
    print(client.email)
    # subject = 'Thank you for registering to our site'
    # message =password
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = ['namatullahwahidi@yahoo.com', ]
    # send_mail(subject, message, email_from, recipient_list)
    clients = Register.objects.all()
    context = {'clients': clients}
    return render(request, 'account/manager.html', context)


def view_aClient(request, id):
    client = get_object_or_404(Register, id=id)
    basic_info = BasicInformation.objects.filter(client=client)
    business = Business.objects.filter(client=client)
    work = Works.objects.filter(client=client)
    credit_line = Credit_line.objects.filter(client=client)
    collateral = Collateral.objects.filter(client=client)
    guarantee = Guarantee.objects.filter(client=client)
    credit_history = Credit_History.objects.filter(client=client)
    context = {
        'client': client,
        'basic_info': basic_info,
        'business': business,
        'work': work,
        'credit_line': credit_line,
        'collateral': collateral,
        'guarantee': guarantee,
        'credit_history': credit_history,
    }
    return render(request, 'clients/client_info.html', context)


class List_AppliedClients(ListView):
    template_name = 'account/manager.html'
    model = Register
    context_object_name = 'applied_clients'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(List_AppliedClients, self).get_context_data(**kwargs)
        context['basic_info'] = BasicInformation.objects.all()
        context['business'] = Business.objects.all()
        context['works'] = Works.objects.all()
        context['credit_line'] = Credit_line.objects.all()
        context['collateral'] = Collateral.objects.all()
        context['guarantee'] = Guarantee.objects.all()
        context['credit_history'] = Credit_History.objects.all()

        return context


class ListClients(ListView):
    template_name = 'account/manager.html'
    model = Register
    context_object_name = 'clients'


def delete_client(request, id):
    article = get_object_or_404(Register, id=id)
    article.delete()
    messages.success(request, "Client  was deleted successfully")
    return redirect("clients:get_client")


def accept_client(request, id):
    client = get_object_or_404(Register, id=id)
    form = AcceptClientForm(request.POST or None)
    basic_info = BasicInformation.objects.filter(client=client)
    credit_line = Credit_line.objects.filter(client=client)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.client = client
        instance.credit_line = get_object_or_404(Credit_line, client=client)
        instance.collateral = get_object_or_404(Collateral, client=client)
        instance.credit_history = get_object_or_404(Credit_History, client=client)
        client1 = Register.objects.filter(pk=client.id)
        instance.client.state = 1
        instance.save()
        for i in client1:
            i.state = 1
            i.save()
        return HttpResponseRedirect(reverse('clients:shared_clients_view'))
    context = {
        'basic_info': basic_info,
        'form': form,
        'credit_line': credit_line,

    }
    return render(request, 'clients/accept_clients.html', context)


def shared_clients_view(request):
    accepted_clients = AcceptClient.objects.all()
    context = {
        'accepted_clients': accepted_clients,
    }
    return render(request, 'clients/shared_clients.html', context)


def SubscribesView(request, id, bankID):
    accept_clients = get_object_or_404(AcceptClient, id=id)
    form = SubscribeForm(request.POST or None)
    subscriber = Subscribe.objects.all()
    bank = get_object_or_404(Register, id=bankID)
    client_rate = accept_clients.credit_line.contribution_amount
    start_rate = accept_clients.start_rate
    object1 = Subscribe.objects.values_list('rate')
    min = object1.order_by('rate').first()
    if min is not None:
        start_rate = min[0]
    # rate = Subscribe.objects.all().aggregate(Min('rate')).get('rate')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.accept_client = accept_clients
        # print("instance type",type(instance.bank))
        print("bank type",type(bank))
        instance.bank = bank
        selected_rate = request.POST['selected_rate']
        instance.rate = selected_rate
        instance.save()
        return HttpResponseRedirect(reverse('clients:subscribe_view', args=(id,bankID,)))

    context = {
        'subscriber': subscriber,
        'accept_client': accept_client,
        'form': form,
        'client_rate': client_rate,
        'start_rate': start_rate,
    }

    return render(request, "clients/subscribe.html", context)
