"""Faça um programa em duas partes:
○ Parte 01: Ler 10 números inteiros e armazená-los em uma lista única.
○ Parte 02: Em uma nova estrutura de repetição, armazene os números pares na
lista PARES e os números ímpares na lista ÍMPARES.
○ Imprima as três listas."""

i = 0
numero = 0
pares = []
impares = []
numeros = []


for i in range(10):
    numero = int(input(f"Digite o número {i+1} de 10: "))
    numeros.append(numero)

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print("Números: ", numeros)
print("Pares: ", pares)
print("Ímpares: ", impares)
