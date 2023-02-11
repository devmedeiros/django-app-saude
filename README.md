# Django App Saúde

## Objetivo

O objetivo era criar um aplicativo capaz de armazenar informações e apresentar-las, utilizando o framework Django. Desta forma eu criei esse aplicativo que seria uma base para um sistema de uma clínica médica, ele conta com três grupos de usuários, cada grupo com permissões diferentes, sendo elas:

| Grupo de Usuário 	| Permissões 	|
|:---:|---	|
| Funcionário | ver pacientes<br />add pacientes<br />alterar pacientes<br />excluir pacientes<br />ver procedimentos<br />add procedimentos<br />alterar procedimentos<br />excluir procedimentos|
| Médico | ver pacientes<br />ver procedimentos<br />add procedimentos<br />alterar procedimentos<br />excluir procedimentos|
| Paciente | ver procedimentos |

## Pré-visualização

## Dados

Os dados do projeto em sua integridade estão disponíveis no sqlite. Todas as informações pessoais são fictícias.

## Rodando localmente

Para rodar o projeto localmente basta clonar o repositório

```bash
  git clone https://github.com/devmedeiros/django-app-saude.git
```

Entre no diretório do projeto

```bash
  cd django-app-saude
```

Instale os pacotes necessários

```bash
  pip install requirements.txt
```

Rode `manage.py`

```bash
  python manage.py runserver
```

### Acessando a aplicação

Todas as pessoas cadastradas no banco de dados possuem usuários cadastrados, seu usuário é formado por sua função (ME, PA, FU) concatenado com o id da pessoa com dois zeros a frente. Então o **Breno Tomás Drummond** que é um **Paciente** (PA) e possui **id = 4**, possui o usuário `pa004`. As senhas são formadas pela funcao do usuário acrescido de seu id com zero a frente, logo a senha do Breno é `paciente04`.

O super usuário criado é `admin` com senha `admin`.

## Stack utilizada

**Back-End:** Django

**DB:** SQLite

**Front-End:** Bootstrap 5

## Referência das Imagens

- forbidden.jpg: [Stop Sign Vectors]("https://www.vecteezy.com/free-vector/stop-sign") by Vecteezy
- procedimentos.jpg: [Imagem de jcomp]("https://br.freepik.com/vetores-gratis/chame-o-conceito-de-medico-os-medicos-respondem-as-perguntas-dos-pacientes-por-telefone_18707003.htm") no Freepik
- pessoas.jpg: [Imagem de pch.vector]("https://br.freepik.com/vetores-gratis/pessoas-multiculturais-juntos_9176081.htm#query=diversidade&position=2&from_view=search&track=sph") no Freepik