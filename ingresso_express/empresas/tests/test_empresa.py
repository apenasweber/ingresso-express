from django.test import TestCase
from empresas.models import Empresa, Endereco, DadosBancarios
from empresas.forms import EmpresaRegistrationForm


class EmpresaModelTest(TestCase):
    def setUp(self):
        self.Empresa = Empresa.objects.create(
            cnpj="12345678901234",
            nome="Empresa de Teste",
            email="test@example.com",
            telefone="123456789",
        )

        self.endereco = Endereco.objects.create(
            empresa=self.Empresa,
            rua="Rua de Teste",
            numero="123",
            cidade="Cidade de Teste",
            estado="Estado de Teste",
            cep="12345678",
        )

        self.dados_bancarios = DadosBancarios.objects.create(
            empresa=self.Empresa,
            tipo_pagamento=DadosBancarios.TIPO_TED,
            banco="001 – Banco do Brasil S.A.",
            agencia="1234",
            conta="123456",
        )

    def test_empresa_creation(self):
        self.assertTrue(isinstance(self.Empresa, Empresa))
        self.assertEquals(self.Empresa.__str__(), self.Empresa.nome)

    def test_endereco_creation(self):
        self.assertTrue(isinstance(self.endereco, Endereco))
        self.assertEquals(
            self.endereco.__str__(),
            f"{self.endereco.rua}, {self.endereco.numero} - {self.endereco.cidade}/{self.endereco.estado}",
        )

    def test_dados_bancarios_creation(self):
        self.assertTrue(isinstance(self.dados_bancarios, DadosBancarios))
        self.assertEquals(
            self.dados_bancarios.__str__(),
            f"{self.dados_bancarios.banco} - {self.dados_bancarios.agencia}/{self.dados_bancarios.conta}",
        )


class EmpresaFormTest(TestCase):
    def test_valid_form(self):
        data = {
            "cnpj": "12345678901234",
            "nome": "Empresa de Teste",
            "email": "test@example.com",
            "telefone": "123456789",
        }
        form = EmpresaRegistrationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            "cnpj": "",
            "nome": "Empresa de Teste",
            "email": "test@example.com",
            "telefone": "123456789",
        }
        form = EmpresaRegistrationForm(data=data)
        self.assertFalse(form.is_valid())
