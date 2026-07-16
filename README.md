# Portfolio Dinamico (CMS Customizado)

Um sistema de gerenciamento de portfolio profissional desenvolvido do zero com Python e Django. Este projeto nao e um simples site estatico em HTML/CSS, mas sim uma aplicacao web completa (estilo CMS) com um painel administrativo seguro, permitindo operacoes de CRUD (Criar, Ler, Atualizar e Deletar) para gerenciar informacoes profissionais, academicas e upload de projetos em tempo real.

O sistema foi arquitetado para ser de facil manutencao e esta hospedado em um ambiente Linux configurado manualmente.

---

## Funcionalidades

*   Painel Administrativo Customizado: Interface de gerenciamento estilizada e intuitiva utilizando o django-jazzmin (Dark Mode).
*   Gestao de Conteudo Dinamico: Adicao, edicao e remocao de projetos, links, textos biograficos e curriculos diretamente pelo painel, sem necessidade de alterar o codigo-fonte.
*   Editor de Texto Rico (WYSIWYG): Integracao com django-tinymce para formatacao avancada de textos nas secoes do portfolio.
*   Processamento de Midia: Upload e renderizacao otimizada de imagens de projetos e arquivos (como PDF para o curriculo) via a biblioteca Pillow.
*   Design Responsivo: A interface publica se adapta perfeitamente a dispositivos moveis e desktops.
*   Seguranca: Autenticacao de rotas no painel administrativo e navegacao segura forcada via HTTPS em producao.

---

## Tecnologias Utilizadas

Back-end & Infraestrutura
*   Python 3.10+
*   Django 5.0.7
*   SQLite3 (Banco de Dados de desenvolvimento e producao inicial)
*   Deploy: PythonAnywhere (Ambiente Linux, Virtualenv, WSGI)

Front-end & UI
*   HTML5 / CSS3
*   Django Jazzmin (Tema do Admin)
*   TinyMCE (Editor de Texto)

---

## Arquitetura e Deploy

O deploy desta aplicacao foi realizado na plataforma PythonAnywhere. O processo envolveu:
1.  Configuracao de um ambiente virtual isolado (virtualenv).
2.  Mapeamento do servidor web via WSGI para comunicacao direta com a aplicacao Django.
3.  Coleta e separacao de arquivos estaticos e de midia (collectstatic) para otimizacao de carregamento atraves do servidor HTTP.
4.  Gerenciamento de versao continuo utilizando o Git e o GitHub.

---

## Como Rodar o Projeto Localmente

Se voce deseja clonar e testar o projeto na sua maquina, siga os passos abaixo:

### Pre-requisitos
*   Python 3.10 ou superior instalado.
*   Git instalado.

### Passo a passo

1. Clone o repositorio:
    git clone https://github.com/SEU_USUARIO/meu-portfolio.git
    cd meu-portfolio

2. Crie e ative o ambiente virtual:
   - Windows:
        python -m venv venv
        venv\Scripts\activate
   - Linux/Mac:
        python3 -m venv venv
        source venv/bin/activate

3. Instale as dependencias:
    pip install -r requirements.txt

4. Realize as migracoes do banco de dados:
    python manage.py migrate

5. Crie um superusuario para acessar o painel administrativo:
    python manage.py createsuperuser

6. Inicie o servidor local:
    python manage.py runserver

7. Acesse no navegador:
   - Site Publico: http://127.0.0.1:8000/
   - Painel Admin: http://127.0.0.1:8000/admin/

---

## Autor

Caio Murilo Silva de Oliveira
Estudante de Engenharia de Software

- LinkedIn: https://linkedin.com/in/murilocaiomurilo/
- Portfolio Online: https://caiomurilo.pythonanywhere.com
