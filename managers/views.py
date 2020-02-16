from abc import ABC

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from managers.forms import ClientRegisterForm, ApplyClientForm
from managers.forms import bankRegister
from managers.models import Client, Bank, FeedFile, ApplyClient


def Home(request):
    return render(request, 'home.html')


def Manager(request):
    return render(request, 'account/manager.html')


def logout(request):
    return redirect("/client")


def ClientRegister(request):
    form = ClientRegisterForm(request.POST or None)
    if form.is_valid():
        new_client = Client()
        new_client.name = form.cleaned_data.get('name')
        new_client.phone = form.cleaned_data.get('phone')
        new_client.message = form.cleaned_data.get('message')
        new_client.save()
        context = {'client': new_client}
        return render(request, 'account/client.html', context)
    context = {'form': form}
    return render(request, 'account/client.html', context)


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
    form = ApplyClientForm(request.POST or None,instance=client)
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


def BankRegister(request):
    form = bankRegister(request.POST or None, request.FILES)
    if form.is_valid():
        newBank = Bank()
        newBank.title = form.cleaned_data.get('title')
        newBank.inn = form.cleaned_data.get('inn')
        newBank.okpo = form.cleaned_data.get('okpo')
        newBank.legalAddress = form.cleaned_data.get('legalAddress')
        newBank.legalAddress1 = form.cleaned_data.get('legalAddress1')
        newBank.responsPerson = form.cleaned_data.get('responsPerson')
        newBank.bankContacts = form.cleaned_data.get('bankContacts')
        newBank.specialistContacts = form.cleaned_data.get('specialistContacts')
        newBank.currentBalance = form.cleaned_data.get('currentBalance')
        newBank.save()
        print(request.FILES.getlist('documents'))
        for f in request.FILES.getlist('documents'):
            file_instance = FeedFile(documents=f, feed=newBank)
            file_instance.save()
            print("saved ok")
        print("saved")
        context = {'bank': newBank}
        return render(request, 'account/bank.html', context)

    context = {'form': form}
    print("here is")
    return render(request, 'account/bank.html', context)


def getBanks(request):
    banks = Bank.objects.all()
    files = FeedFile.objects.all()
    context = {'banks': banks, 'files': files}
    return render(request, 'account/manager.html', context)
