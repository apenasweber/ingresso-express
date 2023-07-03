from empresas.models import Empresa
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Empresa
from .forms import EmpresaForm, LoginForm
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
    return render(request, "empresas/login.html", {"form": form})


@login_required
def dashboard_empresa(request):
    try:
        empresa = Empresa.objects.get(admin=request.user)
        valor_vendido = empresa.get_valor_vendido()
        clientes_nao_expirados = empresa.get_clientes_nao_expirados()
        acessos_pagina_principal = empresa.get_acessos_pagina_principal()
        acessos_atracao = empresa.get_acessos_por_atracao()
        acessos_pacote = empresa.get_acessos_por_pacote()

        return render(
            request,
            "dashboard.html",
            {
                "valor_vendido": valor_vendido,
                "clientes_nao_expirados": clientes_nao_expirados,
                "acessos_pagina_principal": acessos_pagina_principal,
                "acessos_atracao": acessos_atracao,
                "acessos_pacote": acessos_pacote,
            },
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
