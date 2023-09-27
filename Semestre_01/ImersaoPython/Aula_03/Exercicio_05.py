"""5. Faça um programa que leia o nome, idade e altura de 5 pessoas. O sistema deverá
apresentar o nome, idade e altura da pessoa mais alta"""

nome_mais_alto = ""
idade_mais_alto = 0
altura_mais_alto = 0.0

for i in range(0, 5, 1):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))

    if i == 0:
        nome_mais_alto = nome
        idade_mais_alto = idade
        altura_mais_alto = altura

    if altura > altura_mais_alto:
        nome_mais_alto = nome
        idade_mais_alto = idade
        altura_mais_alto = altura

print(f"{nome_mais_alto}, com {idade_mais_alto} anos e {altura_mais_alto:.2f}m, é a pessoa mais alta do grupo.")
