from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Empresa
from .forms import EmpresaForm, AtracaoForm, PacoteForm

@login_required
def registrar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_empresa')
    else:
        form = EmpresaForm()
    return render(request, 'empresas/registrar.html', {'form': form})

@login_required
def login_empresa(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Autenticação e redirecionamento
            return redirect('dashboard_empresa')
    else:
        form = LoginForm()
    return render(request, 'empresas/login.html', {'form': form})

@login_required
def dashboard_empresa(request):
    empresa = Empresa.objects.get(admin=request.user)
    valor_vendido = empresa.get_valor_vendido()
    clientes_nao_expirados = empresa.get_clientes_nao_expirados()
    acessos_pagina_principal = empresa.get_acessos_pagina_principal()
    acessos_atracao = empresa.get_acessos_por_atracao()
    acessos_pacote = empresa.get_acessos_por_pacote()
    
    return render(request, 'empresas/dashboard.html', {
        'valor_vendido': valor_vendido,
        'clientes_nao_expirados': clientes_nao_expirados,
        'acessos_pagina_principal': acessos_pagina_principal,
        'acessos_atracao': acessos_atracao,
        'acessos_pacote': acessos_pacote
    })

@login_required
def adicionar_atracao(request):
    if request.method == 'POST':
        form = AtracaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_empresa')
    else:
        form = AtracaoForm()
    return render(request, 'empresas/adicionar_atracao.html', {'form': form})

@login_required
def adicionar_pacote(request):
    if request.method == 'POST':
        form = PacoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_empresa')
    else:
        form = PacoteForm()
    return render(request, 'empresas/adicionar_pacote.html', {'form': form})

@login_required
def editar_pacote(request, pacote_id):
    pacote = Pacote.objects.get(id=pacote_id)
    if request.method == 'POST':
        form = PacoteForm(request.POST, instance=pacote)
        if form.is_valid():
            form.save()
            return redirect('dashboard_empresa')
    else:
        form = PacoteForm(instance=pacote)
    return render(request, 'empresas/editar_pacote.html', {'form': form})

@login_required
def editar_atracao(request, atracao_id):
    atracao = Atracao.objects.get(id=atracao_id)
    if request.method == 'POST':
        form = AtracaoForm(request.POST, instance=atracao)
        if form.is_valid():
            form.save()
            return redirect('dashboard_empresa')
    else:
        form = AtracaoForm(instance=atracao)
    return render(request, 'empresas/editar_atracao.html', {'form': form})

@login_required
def editar_empresa(request):
    empresa = Empresa.objects.get(admin=request.user)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('dashboard_empresa')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'empresas/editar_empresa.html', {'form': form})

@login_required
def insights_atracao(request, atracao_id):
    atracao = Atracao.objects.get(id=atracao_id)
    # Lógica para obter os insights da atração
    return render(request, 'empresas/insights_atracao.html', {'atracao': atracao})

@login_required
def insights_pacote(request, pacote_id):
    pacote = Pacote.objects.get(id=pacote_id)
    # Lógica para obter os insights do pacote
    return render(request, 'empresas/insights_pacote.html', {'pacote': pacote})

@login_required
def insights_empresa(request):
    empresa = Empresa.objects.get(admin=request.user)
    # Lógica para obter os insights da empresa
    return render(request, 'empresas/insights_empresa.html', {'empresa': empresa})

