from django.contrib.auth import logout
from empresas.models import Empresa
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Empresa
from .forms import EmpresaForm, LoginForm, AtracaoForm, PacoteForm
from django.contrib.auth import authenticate, login


def registrar_empresa(request):
    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("empresas:dashboard_empresa")
    else:
        form = EmpresaForm()
    return render(request, "empresas/registrar.html", {"form": form})


def login_empresa(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("empresas:dashboard_empresa")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


@login_required
def dashboard_empresa(request):
    try:
        return render(
            request,
            "dashboard.html",
        )
    except ObjectDoesNotExist:
        # A empresa não existe
        return render(
            request,
            "dashboard.html",
            {"error_message": "Empresa não encontrada."},
        )


@login_required
def editar_empresa(request):
    empresa = Empresa.objects.get(admin=request.user)
    if request.method == "POST":
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect("empresas:dashboard_empresa")

    else:
        form = EmpresaForm(instance=empresa)
    return render(request, "editar_empresa.html", {"form": form})


@login_required
def criar_atracao(request):
    if request.method == "POST":
        form = AtracaoForm(request.POST)
        if form.is_valid():
            atracao = form.save(commit=False)
            atracao.empresa = Empresa.objects.get(user=request.user)
            atracao.save()
            return redirect("empresas:dashboard_empresa")
    else:
        form = AtracaoForm()
    return render(request, "empresas/criar_atracao.html", {"form": form})


@login_required
def criar_pacote(request):
    if request.method == "POST":
        form = PacoteForm(request.POST)
        if form.is_valid():
            pacote = form.save(commit=False)
            pacote.empresa = Empresa.objects.get(user=request.user)
            pacote.save()
            return redirect("empresas:dashboard_empresa")
    else:
        form = PacoteForm()
    return render(request, "empresas/criar_pacote.html", {"form": form})


# views.py

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect("accounts/login.html")
