def status_aluno(n1, n2):
    media = (n1 + n2)/2
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


# Programa principal
nota_1 = float(input("Digite a nota 1: "))
nota_2 = float(input("Digite a nota 2: "))
status = status_aluno(nota_1, nota_2)
print(status)
