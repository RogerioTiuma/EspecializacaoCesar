"""Escreva um programa que faça a atualização no dicionário numeros_maria de
acordo com os valores de numeros_sara. Porém, ele não deve adicionar novos
valores, só atualizar os existentes. Os dicionários já estão definidos, não é
necessário requerer informações do usuário. São eles:
● numeros_maria = {'a': 100, 'b': 200, 'c': 300}
● numeros_sara = {'a': 300, 'b': 200, 'd': 400, 'c': 500, 'e': 250}"""

numeros_maria = {"a": 100, "b": 200, "c": 300}
numeros_sara = {"a": 300, "b": 200, "d": 400, "c": 500, "e": 250}

numeros_maria["a"] = 300
numeros_maria["c"] = 500

print("Os valores do dicionário numeros_maria são: ", numeros_maria)
