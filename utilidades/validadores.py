import re 

def validar_email(email):
     return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validar_senha(senha):
        if len(senha) < 8:
            return False
        if not re.search(r"[A-Z]", senha):
            return False
        if not re.search(r"[a-z]", senha):
            return False
        if not re.search(r"\d", senha):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
            return False
        return True

def validar_cpf(cpf):
    if not cpf:
        return False
    cpf = re.sub(r"\D", "", cpf)
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False

    def _calc_digit(slice_cpf, factor):
        total = 0
        for ch in slice_cpf:
            total += int(ch) * factor
            factor -= 1
        r = total % 11
        return '0' if r < 2 else str(11 - r)

    d1 = _calc_digit(cpf[:9], 10)
    d2 = _calc_digit((cpf[:9] + d1), 11)
    return cpf[9] == d1 and cpf[10] == d2

def validar_apenas_numeros(valor):
    """Valida se o valor contém apenas números"""
    if not valor:
        return False
    return re.match(r"^\d+$", valor) is not None

def validar_apenas_texto(valor):
    """Valida se o valor contém apenas letras e espaços"""
    if not valor:
        return False
    return re.match(r"^[a-zA-ZáéíóúàâêôãõçÁÉÍÓÚÀÂÊÔÃÕÇ\s]+$", valor) is not None