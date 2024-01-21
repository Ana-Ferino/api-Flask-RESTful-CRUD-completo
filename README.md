# API Flask

Desenvolvida para permitir o gerenciamento de usuários, pessoas e atividades através das rotas e métodos. *

Bancos utilizados:
- [SQLite](https://docs.sqlalchemy.org/en/20/dialects/sqlite.html) para armazenar os dados
- [Redis](https://redis.io/docs/connect/clients/python/) para armazenar os tokens de sessão

A autenticação é realizada de duas formas:
- Com [JWT](https://pyjwt.readthedocs.io/en/stable/)
- Ou com usuário e senha

*Este projeto foi desenvolvido com o propósito de aprendizado e demonstração.

## Iniciando

### Pré-requisitos

Requisitos para o software e outras ferramentas para levantar e testar:
- `Python` >= v3.10
- `Docker-compose` v2.17
- `Docker` v23.0.5

### Configurando o ambiente

```sh
$ git clone https://github.com/{your-username}/flask-crud.git
$ cd .\flask-crud\
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Definindo as variáveis de ambiente

Defina as variáveis para executar a API corretamente. Abaixo está o template:

    SECRECT_KEY_TOKEN=
    SECRECT_KEY_APP_FLASK=
    TIME_EXP_TOKEN_IN_REDIS=
    REDIS_HOST=
    REDIS_PORT=
    REDIS_DB=
    URL_API=http://{{localhost}}:{{port}}


## Executando a API

### Com Docker
```sh
$ docker-compose up --build
```

### Sem Docker
```sh
$ python app.py
```

## Executando os testes
Certifique-se de estar no mesmo diretório do projeto e execute:

```sh
$ pytest
```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
