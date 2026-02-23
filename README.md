# Sistema de Cadastro e Login Universitário

Este é um sistema de Programação Orientada a Objetos (POO) desenvolvido em Python para gerenciar o cadastro de usuários universitários, incluindo discentes, docentes e outros tipos de usuários. O sistema utiliza uma interface web simples construída com JustPy e armazena os dados em arquivos JSON para persistência.

## Estrutura do Projeto

- **classes/**: Contém as classes do sistema (Discente, Docente, Universitario).
- **justPy/**: Interface web da aplicação.
- **persistencia/**: Lógica de persistência de dados em JSON.
- **sistema/**: Lógica principal do sistema de cadastro.
- **testes/**: Scripts de teste.
- **utilidades/**: Utilitários como hash de senha e validadores.

## Pré-requisitos

- Python 3.7 ou superior instalado.
- Dependências: JustPy (para a interface web).

## Instalação e Inicialização

1. Clone ou baixe o repositório para sua máquina.

2. Instale as dependências necessárias:
   ```
   python -m pip install justpy
   ```

3. Navegue até o diretório raiz do projeto.

4. Execute a aplicação:
   ```
   python -m justPy.app
   ```

5. Abra o navegador e acesse `http://localhost:8000` (ou a porta indicada no terminal) para usar o sistema.

## Funcionalidades

- Cadastro de novos usuários (Discente, Docente, etc.).
- Validação de dados e senhas.
- Persistência de dados em JSON.

## Testes

Para executar testes básicos, rode:
```
python testes/main.py
```

Isso criará um usuário de teste no sistema.
