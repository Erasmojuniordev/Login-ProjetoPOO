from utilidades.validadores import validar_senha

class SistemaCadastro:
    
    def __init__(self,repositorio):
        self.__repositorio = repositorio

    def cadastrar(self,usuario,senha,confirmaSenha):

        if senha != confirmaSenha:
            raise ValueError("Senhas não coincidem")

        if not validar_senha(senha):
            raise ValueError("Senha fraca")
        
        if self.__repositorio.buscar_por_cpf(usuario.getCpf()):
            raise ValueError("CPF já cadastrado")
        
        if self.__repositorio.buscar_por_email(usuario.getEmail()):
            raise ValueError("Email já cadastrado")

        self.__repositorio.salvar(usuario)