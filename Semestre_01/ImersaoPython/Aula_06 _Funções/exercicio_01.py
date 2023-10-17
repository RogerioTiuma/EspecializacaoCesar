"""Crie um programa que contenha uma lista de tuplas, onde cada tupla contém o
nome de uma cor e seus valores RGB (Red, Green, Blue), informadas pelo
usuário. Para inserir os valores, o sistema deverá solicitar quantas cores o
usuário deseja informar. Após a inserção, solicite ao usuário que digite o nome
de uma cor e, se a cor estiver na lista, exiba seus valores RGB."""


lista_RGB = []
lista_RGB_unit = []
n = 0
i = 0

n = int(input("Informe o número de cores que dejesa inserir: "))

for i in n:
    cor = input("Qual o valor da cor? ")
    red = input("Qual o número referente ao RED? ")
    green = input("Qual o número referente ao GREEN? ")
    blue = input("Qual o número referente ao BLUE? ")

    lista_RGB_unit.append(cor)
    lista_RGB_unit.append(red)
    lista_RGB_unit.append(green)
    lista_RGB_unit.append(blue)

print(lista_RGB_unit)