# Fluxo v1
1. Representante da empresa acessa página SEJA UM PARCEIRO para disponibilizar suas atrações no totem e preenche um formulário inicial com:
* Nome representante empresa
* email
* telefone
* nome do estabelecimento
* cnpj
* categoria: gastronomia/entretenimento/Hospedagem
* website
* instagram
* capacidade de atendimento
* localidade
* breve descrição do negócio
2. Manualmente os responsáveis pela Ingresso Express adicionarão estas empresas via django admin.
3. Após adicionar estas empresas, email e senha serão enviados aos representantes da empresa para acessarem o sistema Ingresso Express. Em seu primeiro acesso será obrigatório trocar a senha.
4. Logado no sistema, o representante da empresa poderá adicionar atrações, criar pacotes, visualizar infos em sua dashboard, etc.

# User stories
## V1 - Experiência da Empresa

### Admin ingresso express 

 - [x] Como admin ingresso express, eu quero poder adicionar empresa(s)
       para que estas criem suas ofertas e pacotes.

### Admin empresa
-   Como empresa, eu quero poder logar no sistema com email e senha para que eu possa criar ofertas e pacotes.
-   Como empresa, eu quero poder recuperar minha senha para que eu possa logar no sistema.
-   Como empresa eu quero poder editar meus dados cadastrais, com exceção do cnpj, para que eu possa atualizar meus dados.

## Empresa ofertas
-   Como empresa, eu quero poder criar ofertas para que os clientes possam comprar.
-   Como empresa, eu quero poder criar ofertas com data de início e fim para que os clientes possam comprar.
-   Como empresa, eu quero poder visualizar as ofertas que eu criei para que eu possa ver o que eu criei.
-   Como empresa, eu quero poder editar ofertas para que eu possa atualizar os dados.
-   Como empresa, eu quero poder excluir ofertas para que eu possa remover ofertas que não são mais válidas.

# Empresa pacotes

-   Como empresa, eu quero poder criar pacotes para que os clientes possam comprar.
-   Como empresa, eu quero poder criar pacotes com data de início e fim para que os clientes possam comprar.
-   Como empresa, eu quero poder visualizar os pacotes que eu criei para que eu possa ver o que eu criei.
-   Como empresa, eu quero poder editar pacotes para que eu possa atualizar os dados.
-   Como empresa, eu quero poder excluir pacotes para que eu possa remover pacotes que não são mais válidos.

## Empresa vendas

-   Como empresa, eu quero poder visualizar os clientes que compraram minhas ofertas/pacotes para que eu possa ver quem comprou, filtrando pelo nome.
-   Como empresa, eu quero poder visualizar os valores de itens vendidos para que eu possa ver o quanto eu vendi.
-   Como empresa, eu quero poder visualizar os valores de itens vendidos por período para que eu possa ver o quanto eu vendi em um período específico.

# Tasks
1.  Autenticação da empresa (Tags: #Django #DRF #JWT):
    
    -   Criar o modelo Django `Empresa` com os campos relevantes (#Django).
    -   Implementar a rota `POST /api/empresa/login` para autenticação da empresa com JWT (#DRF #JWT).
    -   Implementar a rota `POST /api/empresa/recuperar-senha` para permitir a recuperação de senha (#DRF).
    -   Implementar a rota `PUT /api/empresa/editar` para a edição dos dados cadastrais, exceto CNPJ (#DRF).
    -   Criar testes unitários e de integração para todas as rotas acima (#Pytest).
2.  Gestão de ofertas da empresa (Tags: #Django #DRF):
    
    -   Implementar o modelo Django `Oferta` com os campos relevantes (#Django).
    -   Criar a rota `POST /api/empresa/ofertas` para criar uma nova oferta (#DRF).
    -   Criar a rota `GET /api/empresa/ofertas` para listar todas as ofertas da empresa (#DRF).
    -   Criar a rota `PUT /api/empresa/ofertas/{id}` para editar uma oferta (#DRF).
    -   Criar a rota `DELETE /api/empresa/ofertas/{id}` para excluir uma oferta (#DRF).
    -   Criar testes unitários e de integração para todas as rotas acima (#Pytest).
3.  Gestão de pacotes da empresa (Tags: #Django #DRF):
    
    -   Implementar o modelo Django `Pacote` com os campos relevantes (#Django).
    -   Criar a rota `POST /api/empresa/pacotes` para criar um novo pacote (#DRF).
    -   Criar a rota `GET /api/empresa/pacotes` para listar todos os pacotes da empresa (#DRF).
    -   Criar a rota `PUT /api/empresa/pacotes/{id}` para editar um pacote (#DRF).
    -   Criar a rota `DELETE /api/empresa/pacotes/{id}` para excluir um pacote (#DRF).
    -   Criar testes unitários e de integração para todas as rotas acima (#Pytest).
4.  Gestão de vendas da empresa (Tags: #Django #DRF):
    
    -   Implementar o modelo Django `Venda` com os campos relevantes (#Django).
    -   Criar a rota `GET /api/empresa/vendas` para listar todas as vendas da empresa (#DRF).
    -   Criar a rota `GET /api/empresa/vendas?data_inicial={data_inicial}&data_final={data_final}` para filtrar as vendas por período (#DRF).
    -   Criar testes unitários e de integração para todas as rotas acima (#Pytest).
5.  Implementar as APIs RESTful (Tags: #Django #DRF):
    
    -   Criar os endpoints com Django REST Framework e JWT para autenticação e autorização (#DRF #JWT).
    -   Garantir que todos os endpoints estão devidamente autenticados e autorizados (#DRF #JWT).
    -   Escrever testes de integração para todos os endpoints (#Pytest).

# V2 - Experiência do Cliente Final

## ToTem (Terminal de Autoatendimento)

- Como cliente final, eu quero poder selecionar uma empresa para visualizar as ofertas e pacotes disponíveis para compra.
- Como cliente final, eu quero poder visualizar detalhes de uma oferta ou pacote, incluindo descrição, datas, preços e informações adicionais.
- Como cliente final, eu quero poder adicionar ofertas ou pacotes ao carrinho de compras para posteriormente efetuar o pagamento.
- Como cliente final, eu quero poder visualizar e revisar o carrinho de compras antes de finalizar a compra.
- Como cliente final, eu quero poder efetuar o pagamento das ofertas ou pacotes selecionados utilizando cartões de crédito, débito e pix.
- Como cliente final, eu quero receber um comprovante de compra via email após a conclusão do pagamento.
