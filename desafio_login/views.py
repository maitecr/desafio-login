from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm  
from django.contrib import messages
from django.core.mail import EmailMessage

def UserRegister(request):

    template = "registrar.html"

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            get_form_email = form.cleaned_data["email"]

            send_email = EmailMessage(
                subject= "Cadastro de e-mail concluído",
                body= "E-mail registrado no desagio técnico da Fidelity!",
                #from_email="imlookingforanswer@gmail.com",
                to=[get_form_email],
                )
            
            send_email.send(fail_silently=False)

            messages.success(request, "Usuário criado com sucesso!")
            return redirect('login')
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = CustomUserCreationForm()
    return render(request, template, {"form": form})

def MenuPage(request):
    template = "menu.html"
    if request.method == 'GET':
        return render(request, template, {'user': request.user})