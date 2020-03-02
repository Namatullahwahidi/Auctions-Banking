from abc import ABC

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views import View

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from managers.forms import BankRegisterForm
from managers.models import Bank, FeedFile



def Home(request):
    return render(request, 'home.html')


def Manager(request):
    return render(request, 'account/manager.html')


def logout(request):
    return redirect("/client")


def BankRegister(request):
    form = BankRegisterForm(request.POST or None, request.FILES)

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
        context = {'bank': newBank, 'form': form}
        return render(request, 'account/bank.html', context)

    context = {'form': form}
    print("here is")
    return render(request, 'account/bank.html', context)


def getBanks(request):
    banks = Bank.objects.all()
    files = FeedFile.objects.all()
    context = {'banks': banks, 'files': files}
    return render(request, 'account/manager.html', context)




# class Shared_client_list(ListView):
#     template_name = 'account/manager.html'
#     model = Shared_clients
#     queryset = Shared_clients.objects.filter().order_by('-expire_date')[:1]
#     context_object_name = 'shared_client_list'
