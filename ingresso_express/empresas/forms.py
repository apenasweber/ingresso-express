from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Empresa


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


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
