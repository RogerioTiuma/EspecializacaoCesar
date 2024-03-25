def status_aluno(n1, n2):
    media = (n1 + n2)/2
    if media >= 7:
        return print("Aprovado")
    else:
        return print("Reprovado")


# Programa principal
nota_1 = float(input("Digite a nota 1: "))
nota_2 = float(input("Digite a nota 2: "))
status_aluno(nota_1, nota_2)
