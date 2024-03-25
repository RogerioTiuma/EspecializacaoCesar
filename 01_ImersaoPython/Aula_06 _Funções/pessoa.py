def idade_func():
    ano_atual = int(input("Digite o ano atual: "))
    ano_nasc = int(input("Digite o ano de nascimento: "))
    i = ano_atual-ano_nasc
    return i


def votar(idade):
    if idade >= 16:
        return True
    else:
        return False
