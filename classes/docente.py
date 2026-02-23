from classes.universitario import Universitario

class Docente(Universitario): 
    def __init__(self,nome,cpf,matricula,nascimento,email,senha,departamento):
        super().__init__(nome,cpf,matricula,nascimento,email,senha)
        self.__departamento = departamento

    ### MÉTODO GET ###

    def getDepartamento(self):
        return self.__departamento
    
    ### MÉTODO SET ###

    def setDepartamento(self,departamento):
        self.__departamento = departamento 

    ### SEPARAR PARA O JSON ###

    def to_dict(self):
        dados = super().to_dict()
        dados["departamento"] = self.__departamento
        dados["tipo"] = "Docente"
        return dados