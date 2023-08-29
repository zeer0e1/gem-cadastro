# gem-cadastro

Cadastro de alunos do GEM

## Descrição do projeto

Sistema criado para auxiliar no cadastro de alunos do grupo de estudo músical, que como o nome já diz é um grupo de estudos musicais onde alunos podem aprender a música voltada a música sacra utilizada na congregação cristã no Brasil.

## Como utilizar ?

O projeto foi realizado inicialmente para rodar localmente e para utilizar deve-se possuir um computador com a versão 3.10 do Python.

### Instalação

1.Após a instalação do python baixe/clone o repositório atráves do link 

![imagem1](images_markdown/image1.png)

2.Extraia os arquivos e navegue até a pasta e abra o terminal de sua preferencia e execute o seguinte comando: <br>

<code>python -m venv venv  </code>

Esse código vai criar o ambiente virtual onde vamos executar a aplicação.

3.inicialize o ambiente virtual <br>

<code> . /venv/bin/activate </code>

#### Instalando as dependencias do projeto
1.após inicializar o seu ambiente virtual instale as dependencias do projeto com o comando <br>

<code>pip install -r requiriments.txt </code>
> Esse comando pode variar dependendo do sistema operacional

### Iniciando a aplicação
Antes de iniciar aplicação podemos executar um script feito em python que vai criar alguns dados no banco de dados da aplicação, para executar esse script basta navegar até a pasta utils e executar o arquivo create_alunos <br>

<code> python create_alunos.py </code> <br>

Também devemos criar um usuário admin que vai servir para acessar a area administrativa do djang,para realizar esse cadastro basta executar o comando abaixo e seguir as instruções da tela: <br>

<code> python manger.py createsuperuser </code> <br>

após criar o usuário podemos estar iniciando a aplicação: <br>

<code> python manage.py runserver </code>
## Como utilizar
Ao iniciar a aplicação o usuário será direcionado para a tela de login: <br>

![imagem1](images_markdown/login.png)


Podendo realizar um login caso já tenha um usuário ou criar um, caso o usuário não tenha um login ele pode clicar em Registar e realizar o cadastro: <br>
![imagem1](images_markdown/cadastro_instrutor.png)


Após realizar o cadastro o usuário vai poder acessar a página principal onde contem os gráficos e a página de listagem de alunos: >br>
![imagem1](images_markdown/tela_inicial.png)
![imagem1](images_markdown/lista.png)

## Liberação de acesso 
Por questão de segurança algumas páginas da aplicação só podem ser acessadas após a liberação do usuário como membro da equipe, para realizar isso o usuário deve seguir o passo a passo abaixo:
1- Acessar a página admin do django pelo link: <br>

<code> http://127.0.0.1:8000/admin/ </code>
> para acessar a página deve-se utilizar o usuário criando no inicio da aplicação

2- Acessar a área administrativa e clicar na opções usuários: <br>
![imagem1](images_markdown/user_admin.png)


3- Selecionar o usuário e marcar a seleção onde está escrito "Membro da equipe": <br>

![imagem1](images_markdown/menbro.png)

