"""1.  Faça um algoritmo que leia idades até o usuário digitar -1. O programa deve exibir o
total de idades válidas digitadas, a média das idades, quantas são maiores ou igual a 25
e quantas são menores que 25."""

idade = 0
cont_idades = 0
soma_idades = 0
cont_maiores_25 = 0
cont_menores_25 = 0

while idade != -1:
    idade = int(input("Digite a idade: "))
    if idade == -1:
        continue
    soma_idades += idade
    cont_idades += 1
    if idade >= 25:
        cont_maiores_25 += 1
    else:
        cont_menores_25 += 1

media_idades = soma_idades / cont_idades
print(f"Total de idades: {cont_idades}")
print(f"Média das idades: {media_idades:.2f}")
print(f"Maiores de 25 anos: {cont_maiores_25}")
print(f"Menores de 25 anos: {cont_menores_25}")
