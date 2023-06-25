from django.contrib import admin
from .models import Empresa, Endereco, DadosBancarios

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cnpj', 'email']
    search_fields = ['nome', 'cnpj', 'email']

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['rua', 'numero', 'cidade', 'estado']
    search_fields = ['rua', 'cidade', 'estado']

class DadosBancariosAdmin(admin.ModelAdmin):
    list_display = ['tipo_pagamento', 'banco', 'agencia', 'conta', 'chave_pix']
    search_fields = ['tipo_pagamento', 'banco', 'agencia', 'conta', 'chave_pix']

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(DadosBancarios, DadosBancariosAdmin)
