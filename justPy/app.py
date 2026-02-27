import justpy as jp
import re

from classes.discente import Discente
from classes.docente import Docente
from persistencia.repositorio_json import RepositorioJSON
from sistema.sistemaCadastro import SistemaCadastro
from utilidades.validadores import validar_apenas_numeros, validar_apenas_texto

repo = RepositorioJSON()
sistema = SistemaCadastro(repo)

## PADRONIZAÇÃO DE ESTILOS ##
PAGE = "bg-gray-100 min-h-screen flex items-center justify-center p-6"
CARD = "bg-white w-full max-w-xl rounded-xl shadow-lg p-8"
TITLE = "text-2xl font-bold mb-6"
LABEL = "text-sm font-semibold mt-4"
INPUT = "w-full mt-2 p-2 border rounded focus:outline-none focus:ring"
BTN = "w-full mt-6 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 rounded"
MSG_OK = "mt-4 text-green-700 font-semibold"
MSG_ERR = "mt-4 text-red-700 font-semibold"


def pagina_cadastro():
    wp = jp.WebPage()
    root = jp.Div(classes=PAGE, a=wp)
    card = jp.Div(classes=CARD, a=root)

    jp.Div(text="Cadastro de Usuário", classes=TITLE, a=card)

    ## PADRONIZAÇÃO DA CRIAÇÃO DE CAMPOS ##
    def campo(texto_label, placeholder="", tipo="text"):
        jp.Div(text=texto_label, classes=LABEL, a=card)
        return jp.Input(placeholder=placeholder, type=tipo, classes=INPUT, a=card)
    
    def validar_input_numeros(self, msg):
        self.value = re.sub(r"\D", "", self.value)
    
    def validar_input_texto(self, msg):
        self.value = re.sub(r"[^a-zA-ZáéíóúàâêôãõçÁÉÍÓÚÀÂÊÔÃÕÇ\s]", "", self.value)
    
    def campo_select(texto_label):
        jp.Div(text=texto_label, classes=LABEL, a=card)
        return jp.Select(classes=INPUT, a=card)
    
    def add_options(valor, rota):
        jp.Option(value=valor, text=valor, a=rota)

    ## INPUTS BASICOS ##
    nome = campo("Nome", "Digite seu nome completo")
    nome.on("input", validar_input_texto)

    cpf = campo("CPF", "Somente números (ex: 12345678900)")
    cpf.on("input", validar_input_numeros)

    matricula = campo("Matrícula", "Ex: 20251234")
    matricula.on("input", validar_input_numeros)

    nascimento = campo("Nascimento", tipo="date")
    email = campo("Email", "ex: seuemail@gmail.com", tipo="email")
    senha = campo("Senha", "mín. 6 caracteres", tipo="password")
    confirmar = campo("Confirmar senha", "", tipo="password")

    ## INPUT SELECT ##
    select = campo_select("Tipo de usuário")
    add_options("Discente", select)
    add_options("Docente", select)

    label_extra = jp.Div(text="Curso (discente)", classes=LABEL, a=card)
    extra = jp.Input(placeholder="Ex: Sistemas de Informação", classes=INPUT, a=card)
    extra.on("input", validar_input_texto)

    mensagem = jp.Div(a=card)

    def atualizar_extra(self, msg):
        if select.value == "Discente":
            label_extra.text = "Curso (discente)"
            extra.placeholder = "Ex: Sistemas de Informação"
        else:
            label_extra.text = "Departamento (docente)"
            extra.placeholder = "Ex: Computação"

    ## CASO SELECT SEJA MODIFICADO, ELE RODA A FUNÇÃO DE ATUALIZAR ##
    select.on("change", atualizar_extra)

    def limpar():
        nome.value = ""
        cpf.value = ""
        matricula.value = ""
        nascimento.value = ""
        email.value = ""
        senha.value = ""
        confirmar.value = ""
        extra.value = ""

    def cadastrar(self, msg):
        try:
            ## VERIFICAÇÕES BÁSICAS ##
            if not nome.value or not email.value or not senha.value:
                raise ValueError("Preencha ao menos Nome, Email e Senha.")

            if senha.value != confirmar.value:
                raise ValueError("As senhas não conferem.")

            if select.value == "Discente":
                usuario = Discente(
                    nome.value, cpf.value, matricula.value, nascimento.value,
                    email.value, senha.value, extra.value
                )
            else:
                usuario = Docente(
                    nome.value, cpf.value, matricula.value, nascimento.value,
                    email.value, senha.value, extra.value
                )

            sistema.cadastrar(usuario, senha.value, confirmar.value)

            mensagem.text = "Cadastro realizado com sucesso!"
            mensagem.classes = MSG_OK
            limpar()

        except Exception as erro:
            mensagem.text = str(erro)
            mensagem.classes = MSG_ERR

    btn = jp.Button(text="Cadastrar", classes=BTN, a=card)
    btn.on("click", cadastrar)

    atualizar_extra(None, None)
    return wp


jp.justpy(pagina_cadastro)