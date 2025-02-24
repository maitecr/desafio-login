# desafio_login
Desafio técnico com objetivo de desenvolver uma aplicação para login e registro de usuários, contemplando os campos de nome, e-mail e senha. A autenticação do login deverá ser realizada a partir dos campos e-mail e senha. 

### Tecnologias empregadas:
* Python 3.12.4
* Django 5.1.6
* SQLite3
* HTML5
* CSS3

## TUTORIAL:
Obs.*: Certifique-se de ter o Django e pip instalados em seu sistema.  
Obs.**: Os comandos a seguir são correspondentes ao Sistema Operacional Windows.
### Terminal CLI (será necessário dois terminais):
Terminal CLI 01:
1. Clonar repositório: `git clone https://github.com/maitecr/desafio-login.git`
2. Acessar diretório da aplicação
3. Comando para migrações das tabelas: ```python manage.py migrate```
4. Comando para incluir statics: ```python manage.py collectstatic```
Comando para iniciar aplicação: ```python manage.py runserver```
5. Acessar aplicação através do link fornecido pelo framework + url do admin: `http://127.0.0.1:8000/admin/`
Terminal CLI 02:
1. Comando para instalação de um servidor STMP: ```pip install aiosmtpd```
2. Comando para iniciar servidor STMP local:  ```python -m aiosmtpd --nosetuid --debug --listen localhost:1025```
3. Após o cadastro de usuário, verificar se o servidor retornou neste terminal o e-mail e corpo do texto

### A apllicação possui 3 páginas disponíveis:
1. **Login**:
- url: `http://127.0.0.1:8000/admin/login/`
- Possui 2 campos: e-mail | senha
- Botão "Entrar" para autenticação de usuário, efetuar login e redirecionar para a página "Menu"
- Botão "Registrar" que direciona para a página "Registrar" 

2. **Registrar**
- url: `http://127.0.0.1:8000/registrar/`
- Possui 4 campos: nome, e-mail, senha, confirmar senha
- Botão "Registrar" para cadastrar novo usuário em um Banco de Dados SQLite
- Botão "Cancelar" que retorna à página de login

3. **Menu**
- url: `http://127.0.0.1:8000/menu/`
- Página em que consta o texto "Você está logado" quando a autenticação do usuário tem sucesso e o login é efetuado

## Descrição:
* As funcionalidades exigidas (login e registro de usuário) foram desenvolvidas utilizando o sistema de autenticação já existente no Django, a partir do _User Model_;

1. **Login**:
* A página de login foi sobreescrita e customizada para utilização do campo _e-mail_ para autenticação do usuário, substituindo o campo empregado pelo framework: _username_ ;
* Quando o usuário é autenticado, a página "Menu" é renderizada e informa que o login foi concluído;
* A aplicação autoriza ou impede a autenticação de login do usuário a partir do reconhecimento de e-mail e senha correspondentes. Em caso de erro de autenticação, o usuário será redirecionado para uma página que apresentará uma das seguintes mensagens de erro: (a) 'E-mail inexistente', (b) 'Senha inválida';
* Após a sobreescrita da página, sua interface apresentou desafios em sua customização, impossibilitando retornar as validaçÕes na página presente;
* 

2. **Registro de usuário**:
* O formulário de registro de usuário sofreu customizações para que seus campos correspondam aos requeridos no desafio, a partir do recurso da da classe "UserCreationForm" presente no framework. Adicionalmente, foram inseridas as validações de formulário requisitadas e estão presentes em sua página web;
* 

3. **Extra**:
* Ao finalizar o cadastro de um novo usuário, ele irá receber em sua caixa de entra um e-mail informando que sua conta foi cadastrada no desafio da Fidelity Pesquisas Cadastrais;
* Para envio de e-mail, o frameworkd Django solicita credenciais de um remetente para possibilitar envio de e-mail auntenticado, implicando expor dados sensível no código. A fim de evitar exposição de dados sensíveis, para esta funcionalidade, foi utilizado o protocolo STMP (Simple Mail Transfer Protocol), em que pode-se gerar um servidor local como ambiente de testes para confirmação do envio de e-mail.

