from datetime import timedelta
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            pwd = form.cleaned_data['password']
            obj = form.save()
            obj.set_password(pwd)
            obj.is_staff = False
            obj.save()
            return redirect(reverse('login'))
        return render(request, 'register.html', {'form':form})
    context = {
        'form':RegisterForm()
    }
    return render(request, 'register.html', context)

def user_login(request):
    request.session.set_expiry(timedelta(days=1))
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
            else:
                form._errors['username'] = form.error_class([''])
                form._errors['password'] = form.error_class(['wrong username or password'])
        return render(request, 'login.html', {'form':form})
    context = {
        'form': LoginForm()
    }
    return render(request, 'login.html', context)
    
def user_logout(request):
    logout(request)
    return redirect(reverse('login'))

@login_required(login_url='login')
def users_(request):
    context = {'users': CustomUser.objects.all()}
    print(context['users'])
    return render(request, 'index.html', context)