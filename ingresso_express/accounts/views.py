from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout


from .forms import EmpresaRegistrationForm


def register(request):
    if request.method == "POST":
        form = EmpresaRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Resto do código de redirecionamento após o registro bem-sucedido
    else:
        form = EmpresaRegistrationForm()
    return render(request, "register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("accounts:login")
