import justpy as jp

from classes.discente import Discente
from classes.docente import Docente
from persistencia.repositorio_json import RepositorioJSON
from sistema.sistemaCadastro import SistemaCadastro

# cria sistema
repo = RepositorioJSON()
sistema = SistemaCadastro(repo)


def pagina_cadastro():

    wp = jp.WebPage()
    jp.H1(text="Cadastro de Usuário", a=wp)

    # CAMPOS
    jp.Div(text="Nome:", a=wp)
    nome = jp.Input(a=wp)

    jp.Div(text="CPF:", a=wp)
    cpf = jp.Input(a=wp)

    jp.Div(text="Matrícula:", a=wp)
    matricula = jp.Input(a=wp)

    jp.Div(text="Nascimento:", a=wp)
    nascimento = jp.Input(a=wp)

    jp.Div(text="Email:", a=wp)
    email = jp.Input(a=wp)

    jp.Div(text="Senha:", a=wp)
    senha = jp.Input(type="password", a=wp)

    jp.Div(text="Confirmar senha:", a=wp)
    confirmar = jp.Input(type="password", a=wp)

    # tipo usuário
    jp.Div(text="Tipo de usuário:", a=wp)
    tipo = jp.Select(a=wp)
    jp.Option(value="discente", text="Discente", a=tipo)
    jp.Option(value="docente", text="Docente", a=tipo)

    # campo extra
    label_extra = jp.Div(text="Curso (discente) ou Departamento (docente):", a=wp)
    extra = jp.Input(a=wp)

    # mensagem resultado
    mensagem = jp.Div(a=wp)

    # FUNÇÃO DO BOTÃO
    def cadastrar(self, msg):

        try:
            senha_digitada = senha.value
            confirmar_digitada = confirmar.value

            # cria objeto correto
            if tipo.value == "discente":
                usuario = Discente(
                    nome.value,
                    cpf.value,
                    matricula.value,
                    nascimento.value,
                    email.value,
                    senha_digitada,
                    extra.value
                )
            else:
                usuario = Docente(
                    nome.value,
                    cpf.value,
                    matricula.value,
                    nascimento.value,
                    email.value,
                    senha_digitada,
                    extra.value
                )

            # cadastra no sistema
            sistema.cadastrar(usuario, senha_digitada, confirmar_digitada)

            mensagem.text = "Cadastro realizado com sucesso!"
            mensagem.style = "color: green"

        except Exception as erro:
            mensagem.text = str(erro)
            mensagem.style = "color: red"

    jp.Br(a=wp)
    jp.Button(text="Cadastrar", a=wp, click=cadastrar)

    return wp


jp.justpy(pagina_cadastro)
