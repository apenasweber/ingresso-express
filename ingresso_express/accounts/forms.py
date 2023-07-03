from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from empresas.models import Empresa

User = get_user_model()


class EmpresaRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=200, help_text="Obrigatório. Informe um endereço de email válido."
    )

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] != cd["password2"]:
            raise forms.ValidationError("As senhas não estão iguais.")
        return cd["password2"]

    def save(self, commit=True):
        empresa = super().save(commit=False)
        empresa.user.set_password(self.cleaned_data["password1"])
        if commit:
            empresa.save()
        return empresa


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ["cnpj", "nome", "email", "telefone", "dados_bancarios"]
