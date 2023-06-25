from django.db import models
from empresas.models import Empresa, Atracao, Pacote

class Insight(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    atracao = models.ForeignKey(Atracao, on_delete=models.CASCADE)
    pacote = models.ForeignKey(Pacote, on_delete=models.CASCADE)
    acessos_pagina_principal = models.PositiveIntegerField(default=0)
    acessos_pagina_atracao = models.PositiveIntegerField(default=0)
    acessos_pagina_pacote = models.PositiveIntegerField(default=0)
    vendas_realizadas = models.PositiveIntegerField(default=0)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Insight - {self.data}"
