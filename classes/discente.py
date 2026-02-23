from classes.universitario import Universitario

class Discente(Universitario): 
    def __init__(self,nome,cpf,matricula,nascimento,email,senha,curso):
        super().__init__(nome,cpf,matricula,nascimento,email,senha)
        self.__curso = curso

    ### MÉTODO GET ###

    def getCurso(self):
        return self.__curso
    
    ### MÉTODO SET ###

    def setCurso(self,x):
        self.__curso = x 

    ### SEPARAR PARA O JSON ###

    def to_dict(self):
        dados = super().to_dict()
        dados["curso"] = self.__curso
        dados["tipo"] = "Discente"
        return dados