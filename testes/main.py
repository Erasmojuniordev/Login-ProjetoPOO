from classes.discente import Discente
from persistencia.repositorio_json import RepositorioJSON
from sistema.sistemaCadastro import SistemaCadastro

repo = RepositorioJSON()
sistema = SistemaCadastro(repo)

senha = "SenhaForte1!"

usuario = Discente(
    "João",
    "12345678900",
    "2025001",
    "01/01/2000",
    "joao@email.com",
    senha,
    "Computação"
)

sistema.cadastrar(usuario, senha, senha)

print("Usuário cadastrado com sucesso!")