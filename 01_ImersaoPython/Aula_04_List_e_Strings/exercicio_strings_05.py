"""5. Faça um programa que leia um número de celular, e corrija o número no caso deste
conter somente 8 dígitos, adicionando o '9' na frente. O usuário pode informar o número
com ou sem o traço separador."""

numero = input("Digite o seu número de celular: ")

if numero.find("-") == -1 and len(numero) < 9:
    numero_2 = "9" + numero
elif numero.find("-") != -1 and len(numero) < 10:
    numero_2 = "9" + numero
else:
    numero_2 = numero

print(numero_2)
