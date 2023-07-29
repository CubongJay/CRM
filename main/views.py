from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SignUpForm, AddCustomerForm
from . models import Customer

# Create your views here.


def home(request):

    customers = Customer.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in ......")
            return redirect('home')
    else:
        return render(request, 'home.html', {'customers': customers})


# def login_user(request):
#     pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out succesfully.....")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        # authentocate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have logged in succesfully")
            return redirect('home')
    else:
        form = SignUpForm
    return render(request, 'register.html', {'form': form})


@login_required
def get_customer(request, pk):

    customer = get_object_or_404(Customer, pk=pk)

    return render(request, 'customer.html', {'customer': customer})


@login_required
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    messages.success(request, "Customer Successfully deleted")
    return redirect('home')


def register_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                new_customer = form.save()
                messages.success(request, "Customer record successfully added")
                return redirect('home')

    return render(request, 'new.html', {'form': form})


def update_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = AddCustomerForm(request.POST or None, instance=customer)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, "You have updated the customer record successfully")
            return redirect('home')
        return render(request, 'update_customer.html', {'form': form})
    else:
        return render(request, 'update_customer.html', {'form': form})
