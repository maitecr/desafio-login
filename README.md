Desafio técnico com objetivo de desenvolver uma aplicação para login e registro de usuários, contemplando os campos de nome, e-mail e senha. A autenticação do login deverá ser realizada a partir dos campos e-mail e senha. 

Tecnologias empregadas:
Python 3.12.4
Django 5.1.6
SQLite3
HTML5
CSS3

TUTORIAL:
Obs.: Os comandos a seguir são correspondentes ao Sistema Operacional Windows
Em um terminal CLI:
1. Clonar repositório <git clone https://github.com/maitecr/desafio-login.git>
2. Acessar diretório da aplicação
3. Comando para migrações das tabelas: python manage.py migrate
4. Comando para incluir statics: python manage.py collectstatic
Comando para iniciar aplicação: python manage.py runserver
5. Acessar aplicação através do link fornecido pelo framework + url do admin: <http://127.0.0.1:8000/admin/>

A apllicação terá 3 páginas disponíveis:
1. Login:
- url: admin/login/
- Possui 2 campos: e-mail | senha
- Botão "Entrar" para autenticação de usuário, efetuar login e redirecionar para a página "Menu"
- Botão "Registrar" que direciona para a página "Registrar" 

2. Registrar
- url: registrar/
- Possui 4 campos: nome, e-mail, senha, confirmar senha
- Botão "Registrar" para cadastrar novo usuário em um Banco de Dados SQLite
- Botão "Cancelar" que retorna à página de login

3. Menu
- Página em que costa o texto "Você está logado" quando a autenticação do usuário tem sucesso e o login é efetuado

