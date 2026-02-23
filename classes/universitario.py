from utilidades.validadores import validar_email 
from utilidades.hash_senha import gerar_hash

class Universitario:

    def __init__(self,nome,cpf,matricula,nascimento,email,senha):
        self.__nome = nome 
        self.__cpf = cpf 
        self.__matricula = matricula
        self.__nascimento = nascimento
        self.__email = email
        self.__senha = senha

    ### MÉTODOS GET ###

    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf
    
    def getMatricula(self):
        return self.__matricula
    
    def getNascimento(self):
        return self.__nascimento
    
    def getEmail(self):
        return self.__email
    
    def getSenha(self):
        return self.__senha
    
    ### MÉTODOS SET ###

    def setNome(self,nome):
        self.__nome = nome
    
    def setCpf(self,cpf):
        self.__cpf = cpf

    def setMatricula(self,matricula):
        self.__matricula = matricula

    def setNascimento(self,nascimento):
        self.__nascimento = nascimento

    def setEmail(self,email):
        if not validar_email(email):
            raise ValueError("Email inválido")
        self.__email = email

    def setSenha(self,senha):
        self.__senha = gerar_hash(senha)
        
    ### SEPARAR PARA O JSON ###
    
    def to_dict(self):
        return {
            "nome": self.__nome,
            "cpf": self.__cpf,
            "matricula": self.__matricula,
            "nascimento": self.__nascimento,
            "email": self.__email,
            "senha": self.__senha
        } 


    