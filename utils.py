from models import Pessoas, Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome='Galleani', idade=25)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoas = Pessoas.query.all() 
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.idade)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    pessoa.nome = 'Felipe'
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    consulta_todos_usuarios()
