lista_alunos = []
lista_medias_um = []
lista_medias_dois = []
lista_medias_tres = []

for i in range(3):
    lista_alunos.append(input("Nome aluno: "))
    lista_medias_um.append(float(input("Primeira Média: ")))
    lista_medias_dois.append(float(input("Segunda Média: ")))
    lista_medias_tres.append(float(input("Terceira Média: ")))

for i in range(3):
    media_aluno = (lista_medias_um[i] + lista_medias_dois[i] + lista_medias_tres[i]) / 3

    if media_aluno >= 7:
        print(f"A média de {lista_alunos[i].capitalize()} é {media_aluno:.2f} e ele(a) está aprovado(a).")
    else:   
        print(f"A média de {lista_alunos[i].capitalize()} é {media_aluno:.2f} e ele(a) está reprovado(a).")
