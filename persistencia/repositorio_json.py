import json
import os

class RepositorioJSON:

    def __init__(self, arquivo="usuarios.json"):
        self.__arquivo = arquivo

        if not os.path.exists(self.__arquivo):
            with open(self.__arquivo, "w") as f:
                json.dump([], f)

    def __ler(self):
        with open(self.__arquivo, "r") as f:
            return json.load(f)

    def __escrever(self, dados):
        with open(self.__arquivo, "w") as f:
            json.dump(dados, f, indent=4)

    def salvar(self, usuario):
        dados = self.__ler()
        dados.append(usuario.to_dict())
        self.__escrever(dados)

    def buscar_por_cpf(self, cpf):
        dados = self.__ler()
        for u in dados:
            if u["cpf"] == cpf:
                return u
        return None

    def buscar_por_email(self, email):
        dados = self.__ler()
        for u in dados:
            if u["email"] == email:
                return u
        return None