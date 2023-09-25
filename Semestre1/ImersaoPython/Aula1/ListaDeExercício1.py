"""1. Dado um ângulo em graus, converta-o para radianos.

graus = int(input("Digite um numero em graus para converter em radianos: "))
radianos = graus*(3.14/180)

print(f"\n{graus} graus em radianos é {radianos}")"""

"""2. Peça ao usuário para inserir o valor original de um produto e a porcentagem de
desconto. Calcule e mostre o valor do produto após o desconto. 

valor_do_produto = int(input("Digite o valor original do produto: "))
desconto = int(input("\nDigite o valor do desconto em porcentagem:"))

print(f"\nValor com desconto: R$ {valor_do_produto*(1-(desconto/100))}")"""

""" 3.Dados os lados a, b, e c de um triângulo, calcule sua área. 
a = float(input("Digite o valor do primeiro lado do triângulo:"))
b = float(input("\nDigite o valor do segundo lado do triângulo:"))
c = float(input("\nDigite o valor do terceiro lado do triângulo:"))

s = (a+b+c)/3
area = (s*(s-a)*(s-b)*(s-c))**0.5

print(f"Área do triângulo: {area}")"""

"""4.Peça ao usuário para inserir um valor inicial, a taxa de juro e o tempo. Calcule e
mostre o valor futuro após o período especificado com juros simples.

valor_inicial = float(input("Digite o valor inicial: "))

taxa_de_juros = float(input("Digite a taxa de juros: "))

tempo = float(input("Digite o tempo de parcelamento: "))

print("O valor futuro: ", (valor_inicial+(valor_inicial*taxa_de_juros*tempo)/100))"""

"""5. Escreva um programa que leia o valor total das vendas de um vendedor e a
porcentagem de comissão que ele recebe. Calcule e mostre o valor da comissão.


valor_total = float(input("Digite o valor total: "))

comissao = float(input("Digite o percentual da comissao: "))

print("Valor da Comissão: ", (valor_total*comissao)/100)"""



