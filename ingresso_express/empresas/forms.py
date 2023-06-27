from django import forms
from .models import Empresa, Atracao, Pacote


class AtracaoForm(forms.ModelForm):
    class Meta:
        model = Atracao
        fields = [
            "nome",
            "preco_semana_de",
            "preco_semana_por",
            "preco_fim_semana_de",
            "preco_fim_semana_por",
            "regras",
            "descricao",
            "foto",
            "video",
        ]


class PacoteForm(forms.ModelForm):
    class Meta:
        model = Pacote
        """
            nome = models.CharField(max_length=200)
    atracoes = models.ManyToManyField(Atracao)
    preco_semana_de = models.DecimalField(max_digits=10, decimal_places=2)
    preco_semana_por = models.DecimalField(max_digits=10, decimal_places=2)
    preco_fim_semana_de = models.DecimalField(max_digits=10, decimal_places=2)
    preco_fim_semana_por = models.DecimalField(max_digits=10, decimal_places=2)
    regras = models.TextField()
    descricao = models.TextField()
    foto = models.ImageField(upload_to='pacote_fotos/')
    video = models.URLField()
        """
        fields = [
            "nome",
            "atracoes",
            "preco_semana_de",
            "preco_semana_por",
            "preco_fim_semana_de",
            "preco_fim_semana_por",
            "regras",
            "descricao",
            "foto",
            "video",
        ]


class EmpresaRegistrationForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ["cnpj", "nome", "email", "telefone", "dados_bancarios"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Empresa.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

    def save(self, commit=True):
        empresa = super().save(commit=False)
        if commit:
            empresa.save()
        return empresa


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            "cnpj",
            "nome",
            "email",
            "telefone",
            "dados_bancarios",
        ]

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "cnpj": forms.TextInput(attrs={"class": "form-control"}),
            "enderecos": forms.Textarea(attrs={"class": "form-control"}),
            "cidade": forms.TextInput(attrs={"class": "form-control"}),
            "estado": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telefone": forms.TextInput(attrs={"class": "form-control"}),
            "forma_pagamento": forms.Select(attrs={"class": "form-control"}),
            "banco": forms.TextInput(attrs={"class": "form-control"}),
            "agencia": forms.TextInput(attrs={"class": "form-control"}),
            "conta": forms.TextInput(attrs={"class": "form-control"}),
            "chave_pix": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_chave": forms.Select(attrs={"class": "form-control"}),
        }
