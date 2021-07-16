from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.models import Account
from accounts.forms import RegistrationForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Account.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            return redirect('login')

    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            # messages.error('Invalid login credentials!')
            return redirect('login')
    return render(request, 'auth/login.html', {})


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')