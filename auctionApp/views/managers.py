from django.shortcuts import render, redirect

from auctionApp.models import Register
from auctionApp.forms import BankRegisterForm
from auctionApp.models import Bank, FeedFile


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
        newBank.L_addr = form.cleaned_data.get('L_addr')
        newBank.L_addr1 = form.cleaned_data.get('L_addr1')
        newBank.R_person = form.cleaned_data.get('R_person')
        newBank.B_contact = form.cleaned_data.get('B_contact')
        newBank.S_contact = form.cleaned_data.get('S_contact')
        newBank.currentBalance = form.cleaned_data.get('currentBalance')
        newBank.save()
        username = form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = Register.objects.create(username=username, password=password,email=email,is_bank=True)
        user.save()
        print(request.FILES.getlist('documents'))
        for f in request.FILES.getlist('documents'):
            file_instance = FeedFile(documents=f, feed=newBank)
            file_instance.save()
        context = {'bank': newBank, 'form': form}
        return redirect('managers:manager')
    context = {'form': form}
    return render(request, 'account/bank.html', context)


# class BankRegister(CreateView):
#     model = Bank
#     form_class = BankRegisterForm
#     template_name = '../templates/clients/sign_up.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'bank'
#         return super().get_context_data(**kwargs)


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
