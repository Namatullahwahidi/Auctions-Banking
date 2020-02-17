
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, CreateView
from clients.models import Client, ApplyClient
from clients.forms import ClientRegisterForm, ApplyClientForm,LoginForm


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
        # UserTest=Register(email=email,password=password)
        user = Client.objects.filter(email=email, password=password).values()
        for share in user:
            print(share['name'])
        if (not user):
            messages.info(request, "Email or password is invalid")
            return render(request, 'users/login.html', context)
        else:
            messages.success(request, "Successfully inserted")
            user1 = ""
            fs = FileSystemStorage()
            for u in user:
                user1 = u
                # imageName=fs.save()
            context = {'newUser': user1}
            return render(request, 'index1.html', context)
    return render(request, "users/login.html", context)


class ListClients(ListView):
    template_name = 'account/manager.html'
    model = Client
    context_object_name = 'clients'


def delete_client(request, id):
    article = get_object_or_404(Client, id=id)
    article.delete()
    messages.success(request, "Client  was deleted successfully")
    return redirect("managers:get_client")


def apply_client(request, id):
    client = get_object_or_404(Client, id=id)
    client_form = ClientRegisterForm(request.POST or None, instance=client)
    form = ApplyClientForm(request.POST or None, instance=client)
    print(form.is_valid())
    if form.is_valid():
        instance = ApplyClient()
        instance.client = client
        instance.dealTime = form.cleaned_data.get('dealTime')
        instance.credit_purpose = form.cleaned_data.get('credit_purpose')
        instance.credit_amount = form.cleaned_data.get('credit_amount')
        instance.collateral = form.cleaned_data.get('collateral')
        instance.credit_history = form.cleaned_data.get('credit_history')
        instance.finan_perfor = form.cleaned_data.get('finan_perfor')
        instance.dealTime = form.cleaned_data.get('dealTime')
        instance.dealTime = form.cleaned_data.get('dealTime')
        instance.save()

        return redirect("managers:manager")
    return render(request, "account/apply_client.html", {"form": form, 'client_form': client_form})


class List_AppliedClients(ListView):
    template_name = 'account/manager.html'
    model = ApplyClient
    context_object_name = 'applied_clients'
