from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import FormRegistro, FormLogin
from .models import User

# Create your views here.

def user_registro(request):
    if request.method == 'POST':
        form = FormRegistro(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            if password == password2:
                User.objects.create(
                    username=username,
                    nombre=nombre,
                    apellido=apellido,
                    email=email,
                    telefono=telefono,
                    password=password
                )
                return redirect('login')
            else:
                return redirect('registro')
    return render(request, 'accounts/registro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form = FormLogin()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')
