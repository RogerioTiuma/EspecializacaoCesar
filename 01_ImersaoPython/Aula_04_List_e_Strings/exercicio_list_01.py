"""
1. Faça um programa que leia um número indeterminado de valores, correspondentes a
idades, encerrando a entrada de dados quando for informado um valor igual a -1 (que
não deve ser armazenado). Após esta entrada de dados, faça:

○ Mostre a quantidade de idades válidas;
○ Exiba as idades armazenadas;
○ Calcule e mostre a média das idades;
○ Calcule e mostre a quantidade de idades acima da média calculada;
○ Exiba a maior e menor idade;
○ Calcule e mostre a quantidade de valores abaixo de 18.
"""
i = 0
j = 0
count1 = 0
count2 = 0
idades = []
digitado = 0

# Insere valores
while digitado != -1:
    digitado = int(input("Insira uma idade ou -1 para Sair: \n"))

    if digitado != -1:
        idades.append(digitado)
        i += 1

# Conta valores acima da média
for j in idades:
    if j > sum(idades)/len(idades):
        count1 += 1

# Conta valores abaixo de 18
for j in idades:
    if j < 18:
        count2 += 1

print("\nQuantidade de idades válidas: ", i)
print("Idades armazenadas: ", idades)
print("Média das idades: ", sum(idades)/len(idades))
print("Quant. de idades acima da média: ", count1)
print("Maior idade: ", max(idades))
print("Menor idade: ", min(idades))
print("Quant. de idades abaixo de 18: ", count2)
print(" ")
