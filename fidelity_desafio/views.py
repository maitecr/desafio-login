from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm  
from django.contrib import messages
from django.contrib.auth import views as auth_views


def registrar_usuario(request):

    template = "registrar.html"

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criado com sucesso!")
            return redirect('login')
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = CustomUserCreationForm()
    return render(request, template, {"form": form})


def menu_page(request):
    template = "menu.html"
    if request.method == 'GET':
        return render(request, template, {'user': request.user})