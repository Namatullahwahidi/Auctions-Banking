from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, CreateView, TemplateView
from django.db.models import Min
from clients.forms import ClientRegisterForm, LoginForm
from django.contrib.auth.base_user import BaseUserManager
from clients.forms import BasicInformationForm, BusinessForm, AcceptClientForm, \
    WorksForm, Credit_LineForm, CollateralForm, GuaranteeForm, Credit_HistoryForm, SubscribeForm
from clients.models import Client, BasicInformation, Business, Works, Credit_line, \
    Collateral, Guarantee, Credit_History, AcceptClient, Subscribe
from managers.models import Bank


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
            return HttpResponseRedirect(reverse('clients:basic_view', args=(id,)))
    return render(request, "clients/login.html", context)


def BasicView(request, id):
    client = get_object_or_404(Client, id=id)
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
    client = get_object_or_404(Client, id=id)
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
    client = get_object_or_404(Client, id=id)
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
    client = get_object_or_404(Client, id=id)
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
    client = get_object_or_404(Client, id=id)
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
    client = get_object_or_404(Client, id=id)
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
    client = get_object_or_404(Client, id=id)
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
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'account/manager.html', context)


def view_aClient(request, id):
    client = get_object_or_404(Client, id=id)
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
    model = Client
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
    model = Client
    context_object_name = 'clients'


def delete_client(request, id):
    article = get_object_or_404(Client, id=id)
    article.delete()
    messages.success(request, "Client  was deleted successfully")
    return redirect("clients:get_client")


def accept_client(request, id):
    client = get_object_or_404(Client, id=id)
    form = AcceptClientForm(request.POST or None)
    basic_info = BasicInformation.objects.filter(client=client)
    credit_line = Credit_line.objects.filter(client=client)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.client = client
        instance.credit_line = get_object_or_404(Credit_line, client=client)
        instance.collateral = get_object_or_404(Collateral, client=client)
        instance.credit_history = get_object_or_404(Credit_History, client=client)
        client1 = Client.objects.filter(pk=client.id)
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
        'accepted_clients': accepted_clients
    }
    return render(request, 'clients/shared_clients.html', context)


def SubscribesView(request, id):
    accept_client = get_object_or_404(AcceptClient, id=id)
    form = SubscribeForm(request.POST or None)
    subscriber = Subscribe.objects.all()
    bank = get_object_or_404(Bank, id=3)
    client_rate=accept_client.credit_line.contribution_amount
    start_rate=accept_client.start_rate
    object1= Subscribe.objects.values_list('rate')
    min=object1.order_by('rate').first()
    if min is not None:
        start_rate=min[0]

    # print(min[0])
    # rate = Subscribe.objects.all().aggregate(Min('rate')).get('rate')
    # print(rate)
    # if rate is None:
    #     print(rate)
    # else:
    #     print(rate)
    # bank=Bank.objects.all()
    # for i in bank:
    #     print(i.id)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.accept_client = accept_client
        instance.bank = bank
        selected_rate=request.POST['selected_rate']
        instance.rate=selected_rate
        # print(selected_rate)
        instance.save()
        # print(start_rate)
        return HttpResponseRedirect(reverse('clients:subscribe_view', args=(id,)))

    context = {
        'subscriber': subscriber,
        'accept_client': accept_client,
        'form': form,
        'client_rate':client_rate,
        'start_rate':start_rate,
    }

    return render(request, "clients/subscribe.html", context)

# https://stackoverflow.com/questions/569468/django-multiple-models-in-one-template-using-forms
# class PrimaryForm(ModelForm):
#     class Meta:
#         model = Primary
#
#
# class BForm(ModelForm):
#     class Meta:
#         model = B
#         exclude = ('primary',)
#
#
# class CForm(ModelForm):
#     class Meta:
#         model = C
#         exclude = ('primary',)
#
#
# def generateView(request):
#     if request.method == 'POST':  # If the form has been submitted...
#         primary_form = PrimaryForm(request.POST, prefix="primary")
#         b_form = BForm(request.POST, prefix="b")
#         c_form = CForm(request.POST, prefix="c")
#         if primary_form.is_valid() and b_form.is_valid() and c_form.is_valid():  # All validation rules pass
#             print
#             "all validation passed"
#             primary = primary_form.save()
#             b_form.cleaned_data["primary"] = primary
#             b = b_form.save()
#             c_form.cleaned_data["primary"] = primary
#             c = c_form.save()
#             return HttpResponseRedirect("/viewer/%s/" % (primary.name))
#         else:
#             print
#             "failed"
#
#     else:
#         primary_form = PrimaryForm(prefix="primary")
#         b_form = BForm(prefix="b")
#         c_form = Form(prefix="c")
#
#
# return render_to_response('multi_model.html', {
#     'primary_form': primary_form,
#     'b_form': b_form,
#     'c_form': c_form,
# })
