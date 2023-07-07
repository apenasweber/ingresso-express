from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User


class Empresa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    cnpj = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    telefone = models.CharField(max_length=20)
    dados_bancarios = models.OneToOneField(
        "DadosBancarios",
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
        related_name="rel_empresa",
    )

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    empresa = models.ForeignKey("Empresa", on_delete=models.CASCADE, default=None)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado}"


BANCO_CHOICES = [
    ("001", "001 – Banco do Brasil S.A."),
    ("033", "033 – Banco Santander"),
    ("104", "104 – Caixa Econômica Federal"),
    ("237", "237 – Banco Bradesco S.A."),
    ("341", "341 – Banco Itaú S.A."),
    ("356", "356 – Banco Real S.A. "),
    ("389", "389 – Banco Mercantil do Brasil S.A."),
    ("399", "399 – HSBC Bank Brasil S.A. – Banco Múltiplo"),
    ("422", "422 – Banco Safra S.A."),
    ("453", "453 – Banco Rural S.A."),
    ("633", "633 – Banco Rendimento S.A."),
    ("652", "652 – Itaú Unibanco Holding S.A."),
    ("745", "745 – Banco Citibank S.A."),
    ("246", "246 – Banco ABC Brasil S.A."),
    ("025", "025 – Banco Alfa S.A."),
    ("641", "641 – Banco Alvorada S.A."),
    ("029", "029 – Banco Banerj S.A."),
    ("038", "038 – Banco Banestado S.A."),
    ("000", "000 – Banco Bankpar S.A."),
    ("740", "740 – Banco Barclays S.A."),
    ("107", "107 – Banco BBM S.A."),
    ("031", "031 – Banco Beg S.A."),
    ("096", "096 – Banco BM&F de Serviços de Liquidação e Custódia S.A"),
    ("318", "318 – Banco BMG S.A."),
    ("752", "752 – Banco BNP Paribas Brasil S.A."),
    ("248", "248 – Banco Boavista Interatlântico S.A."),
    ("036", "036 – Banco Bradesco BBI S.A."),
    ("204", "204 – Banco Bradesco Cartões S.A."),
    ("225", "225 – Banco Brascan S.A."),
    ("044", "044 – Banco BVA S.A."),
    ("263", "263 – Banco Cacique S.A."),
    ("473", "473 – Banco Caixa Geral – Brasil S.A."),
    ("222", "222 – Banco Calyon Brasil S.A."),
    ("040", "040 – Banco Cargill S.A."),
    ("M08", "M08 – Banco Citicard S.A."),
    ("M19", "M19 – Banco CNH Capital S.A."),
    ("215", "215 – Banco Comercial e de Investimento Sudameris S.A."),
    ("756", "756 – Banco Cooperativo do Brasil S.A. – BANCOOB"),
    ("748", "748 – Banco Cooperativo Sicredi S.A."),
    ("505", "505 – Banco Credit Suisse"),
    ("229", "229 – Banco Cruzeiro do Sul S.A."),
    ("003", "003 – Banco da Amazônia S.A."),
    ("083-3", "083-3 – Banco da China Brasil S.A."),
    ("707", "707 – Banco Daycoval S.A."),
    ("M06", "M06 – Banco de Lage Landen Brasil S.A."),
    ("024", "024 – Banco de Pernambuco S.A. – BANDEPE"),
    ("456", "456 – Banco de Tokyo-Mitsubishi UFJ Brasil S.A."),
    ("214", "214 – Banco Dibens S.A."),
    ("047", "047 – Banco do Estado de Sergipe S.A."),
    ("037", "037 – Banco do Estado do Pará S.A."),
    ("041", "041 – Banco do Estado do Rio Grande do Sul S.A."),
    ("004", "004 – Banco do Nordeste do Brasil S.A."),
    ("265", "265 – Banco Fator S.A."),
    ("M03", "M03 – Banco Fiat S.A."),
    ("224", "224 – Banco Fibra S.A."),
    ("626", "626 – Banco Ficsa S.A."),
    ("394", "394 – Banco Finasa BMC S.A."),
    ("M18", "M18 – Banco Ford S.A."),
    ("233", "233 – Banco GE Capital S.A."),
    ("734", "734 – Banco Gerdau S.A."),
    ("M07", "M07 – Banco GMAC S.A."),
    ("612", "612 – Banco Guanabara S.A."),
    ("M22", "M22 – Banco Honda S.A."),
    ("063", "063 – Banco Ibi S.A. Banco Múltiplo"),
    ("M11", "M11 – Banco IBM S.A."),
    ("604", "604 – Banco Industrial do Brasil S.A."),
    ("320", "320 – Banco Industrial e Comercial S.A."),
    ("653", "653 – Banco Indusval S.A."),
    ("630", "630 – Banco Intercap S.A."),
    ("249", "249 – Banco Investcred Unibanco S.A."),
    ("184", "184 – Banco Itaú BBA S.A."),
    ("479", "479 – Banco ItaúBank S.A"),
    ("M09", "M09 – Banco Itaucred Financiamentos S.A."),
    ("376", "376 – Banco J. P. Morgan S.A."),
    ("074", "074 – Banco J. Safra S.A."),
    ("217", "217 – Banco John Deere S.A."),
    ("065", "065 – Banco Lemon S.A."),
    ("600", "600 – Banco Luso Brasileiro S.A."),
    ("755", "755 – Banco Merrill Lynch de Investimentos S.A."),
    ("746", "746 – Banco Modal S.A."),
    ("151", "151 – Banco Nossa Caixa S.A."),
    ("045", "045 – Banco Opportunity S.A."),
    ("623", "623 – Banco Panamericano S.A."),
    ("611", "611 – Banco Paulista S.A."),
    ("643", "643 – Banco Pine S.A."),
    ("638", "638 – Banco Prosper S.A."),
    ("747", "747 – Banco Rabobank International Brasil S.A."),
    ("M16", "M16 – Banco Rodobens S.A."),
    ("072", "072 – Banco Rural Mais S.A."),
    ("250", "250 – Banco Schahin S.A."),
    ("749", "749 – Banco Simples S.A."),
    ("366", "366 – Banco Société Générale Brasil S.A."),
    ("637", "637 – Banco Sofisa S.A."),
    ("464", "464 – Banco Sumitomo Mitsui Brasileiro S.A."),
    ("082-5", "082-5 – Banco Topázio S.A."),
    ("M20", "M20 – Banco Toyota do Brasil S.A."),
    ("634", "634 – Banco Triângulo S.A."),
    ("208", "208 – Banco UBS Pactual S.A."),
    ("M14", "M14 – Banco Volkswagen S.A."),
    ("655", "655 – Banco Votorantim S.A."),
    ("610", "610 – Banco VR S.A."),
    ("370", "370 – Banco WestLB do Brasil S.A."),
    ("021", "021 – BANESTES S.A. Banco do Estado do Espírito Santo"),
    ("719", "719 – Banif-Banco Internacional do Funchal"),
    ("073", "073 – BB Banco Popular do Brasil S.A."),
    ("078", "078 – BES Investimento do Brasil S.A.-Banco de Investimento"),
    ("069", "069 – BPN Brasil Banco Múltiplo S.A."),
    ("070", "070 – BRB – Banco de Brasília S.A."),
    ("477", "477 – Citibank N.A."),
    ("081-7", "081-7 – Concórdia Banco S.A."),
    ("487", "487 – Deutsche Bank S.A. – Banco Alemão"),
    ("751", "751 – Dresdner Bank Brasil S.A. – Banco Múltiplo"),
    ("062", "062 – Hipercard Banco Múltiplo S.A."),
    ("492", "492 – ING Bank N.V."),
    ("488", "488 – JPMorgan Chase Bank"),
    ("409", "409 – UNIBANCO – União de Bancos Brasileiros S.A."),
    ("230", "230 – Unicard Banco Múltiplo S.A."),
]


class DadosBancarios(models.Model):
    empresa = models.OneToOneField(
        Empresa,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="rel_dados_bancarios",
    )
    TIPO_TED = "TD"
    TIPO_PIX = "PX"
    TIPO_PAGAMENTO = [
        (TIPO_TED, "TED"),
        (TIPO_PIX, "PIX"),
    ]

    tipo_pagamento = models.CharField(
        max_length=2,
        choices=TIPO_PAGAMENTO,
        default=TIPO_TED,
    )

    banco = models.CharField(max_length=50, null=True, blank=True)
    agencia = models.CharField(max_length=10, null=True, blank=True)
    conta = models.CharField(max_length=20, null=True, blank=True)

    CHAVE_CELULAR = "CL"
    CHAVE_CNPJ = "CJ"
    CHAVE_EMAIL = "EM"
    CHAVE_ALEATORIA = "AL"

    TIPO_CHAVE_PIX = [
        (CHAVE_CELULAR, "Celular"),
        (CHAVE_CNPJ, "CNPJ"),
        (CHAVE_EMAIL, "Email"),
        (CHAVE_ALEATORIA, "Chave Aleatória"),
    ]

    chave_pix = models.CharField(max_length=255, null=True, blank=True)
    tipo_chave_pix = models.CharField(
        max_length=2,
        choices=TIPO_CHAVE_PIX,
        default=CHAVE_ALEATORIA,
        null=True,
        blank=True,
    )

    def clean(self):
        if not self.empresa:
            raise ValidationError(
                "Um DadosBancarios deve estar associado a uma Empresa."
            )

    def __str__(self):
        if self.tipo_pagamento == self.TIPO_TED:
            return f"{self.banco} - {self.agencia}/{self.conta}"
        else:
            return f"{self.get_tipo_chave_pix_display()}: {self.chave_pix}"


class Atracao(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco_fim_de_semana = models.DecimalField(
        max_digits=7, decimal_places=2, validators=[MinValueValidator(Decimal("0"))]
    )
    preco_feriado = models.DecimalField(
        max_digits=7, decimal_places=2, validators=[MinValueValidator(Decimal("0"))]
    )
    data_expiracao = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Pacote(models.Model):
    nome = models.CharField(max_length=200)
    atracoes = models.ManyToManyField(Atracao)
    preco_fim_de_semana = models.DecimalField(
        max_digits=7, decimal_places=2, validators=[MinValueValidator(Decimal("0"))]
    )
    preco_feriado = models.DecimalField(
        max_digits=7, decimal_places=2, validators=[MinValueValidator(Decimal("0"))]
    )
    data_expiracao = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome
