# API de E-commerce

Esta é uma API de e-commerce desenvolvida em Django, que oferece funcionalidades essenciais para uma plataforma de e-commerce. Com apps específicos para cada recurso, a API permite gerenciar produtos, usuários, pedidos, pagamentos e avaliações.

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework:** Django
- **Banco de Dados:** SQLite (Inicialmente foi feito em PostgreSQL, porém mudou depois para fazer o deploy)
- **Autenticação:** Simple JWT
- **Deploy:** PythonAnywhere
- **Integração de Pagamento:** API do Mercado Pago

## Funcionalidades Principais

A API possui os seguintes apps, cada um operando em um endpoint correspondente:

- **Produtos:** Gerenciamento de itens disponíveis na loja.
- **Pagamentos:** Processamento de pagamentos, integrando com a API do Mercado Pago.
- **Pedidos:** Controle de pedidos dos clientes.
- **Usuários:** Registro e autenticação de usuários.
- **Favoritos:** Permite que os usuários marquem produtos como favoritos.
- **Avaliações:** Sistema de avaliação de produtos pelos usuários.
- **Categorias:** Classificação de produtos em diferentes categorias.

## Endpoints

Cada app possui um endpoint próprio, facilitando a organização e a manutenção da API. 

### Endpoints Principais

- `api/v1/produtos/` - Endpoint para listagem e detalhes de produtos.
- `api/v1/pagamentos/` - Endpoint para gerenciamento e processamento de pagamentos.
- `api/v1/pedidos/` - Endpoint para criação e visualização de pedidos.
- `api/v1/itens-carrinho/` - Endpoint para adição de produtos a um pedido.
- `api/v1/usuarios/` - Endpoint para registro e autenticação de usuários.
- `api/v1/perfis/` - Endpoint para registro de um perfil para um usuário.
- `api/v1/favoritos/` - Endpoint para gestão dos produtos favoritos dos usuários.
- `api/v1/avaliacoes/` - Endpoint para avaliação de produtos.
- `api/v1/categorias/` - Endpoint para classificação dos produtos.
- `api/v1/authentication/token/` - Endpoint para criar o token de acesso a API.
- `api/v1/authentication/token/verify/` - Endpoint para verificar se o token ainda é válido.
- `api/v1/authentication/token/refresh` - Endpoint para atualizar o token para que o usuário continue autenticado sem precisar fazer login novamente.

## Autenticação

A API utiliza **Simple JWT** para autenticação, garantindo segurança nas operações sensíveis. Para acessar certos endpoints, é necessário um token de autenticação obtido via login.

## Configuração e Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/LuizH0412/e-commerce.git
    cd e-commerce
    ```

2. Crie e ative um ambiente virtual:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use: venv\Scripts\activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Realize as migrações:

    ```bash
    python manage.py migrate
    ```

5. Inicie o servidor localmente:

    ```bash
    python manage.py runserver
    ```
