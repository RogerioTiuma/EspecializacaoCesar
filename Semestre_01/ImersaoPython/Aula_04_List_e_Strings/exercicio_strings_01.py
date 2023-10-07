""" 1. Faça um programa que receba um e-mail e verifique se ele é válido. Obs: Para um
e-mail ser válido considerar se possui “@”."""

email = input("Digite um e-mail válido (Com @): ")

if email.find('@') != -1:
    print("E-mail válido.")
else:
    print("E-mail inválido.")

