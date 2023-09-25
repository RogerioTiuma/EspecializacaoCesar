"""1. Dado um ângulo em graus, converta-o para radianos.

graus = int(input("Digite um numero em graus para converter em radianos: "))
radianos = graus*(3.14/180)
print(f"\n{graus} graus em radianos é {radianos}")

2. Peça ao usuário para inserir o valor original de um produto e a porcentagem de
desconto. Calcule e mostre o valor do produto após o desconto. 

valor_do_produto = int(input("Digite o valor original do produto: "))
desconto = int(input("\nDigite o valor do desconto em porcentagem:"))
print(f"\nValor com desconto: R$ {valor_do_produto*(1-(desconto/100))}")

3.Dados os lados a, b, e c de um triângulo, calcule sua área.

a = float(input("Digite o valor do primeiro lado do triângulo:"))
b = float(input("\nDigite o valor do segundo lado do triângulo:"))
c = float(input("\nDigite o valor do terceiro lado do triângulo:"))
s = (a+b+c)/3
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(f"Área do triângulo: {area}")

4.Peça ao usuário para inserir um valor inicial, a taxa de juro e o tempo. Calcule e
mostre o valor futuro após o período especificado com juros simples.

valor_inicial = float(input("Digite o valor inicial: "))
taxa_de_juros = float(input("Digite a taxa de juros: "))
tempo = float(input("Digite o tempo de parcelamento: "))
print("O valor futuro: ", (valor_inicial+(valor_inicial*taxa_de_juros*tempo)/100))

5. Escreva um programa que leia o valor total das vendas de um vendedor e a
porcentagem de comissão que ele recebe. Calcule e mostre o valor da comissão.

valor_total = float(input("Digite o valor total: "))
comissao = float(input("Digite o percentual da comissao: "))
print("Valor da Comissão: ", (valor_total*comissao)/100)

6. Dado um raio r e calcule e mostre a área de um círculo.

raio = int(input("Forneça o valor do raio:"))
Area = 3.14*(raio**2)
print("Área do círculo: ", Area)

7. Escreva um programa que leia o custo de produção de um produto e seu preço de
venda. Calcule e mostre o lucro bruto obtido na venda do produto.

custo_de_producao = int(input("Qual o valor do custo de produção? "))
lucro_bruto = int(input("Qual o valor do lucro bruto? "))
print("Lucro Bruto: R$", lucro_bruto-custo_de_producao)

8. Converta uma temperatura em graus Celsius C para Fahrenheit F.

temperatura_celsius = int(input("Informe a temperatura em celsius para transformar em Fahrenheit F: "))
F = 9/5*temperatura_celsius+32
print(f"{temperatura_celsius} graus Celsius é {F} graus Fahrenheit.")

9. Peça ao usuário para inserir o valor de um produto e a taxa de imposto aplicada sobre
ele. Calcule e mostre o valor final do produto com o imposto.

valor_do_produto = float(input("Informe o valor do produto:"))
taxa_de_imposto = float(input("Informe a taxa: "))
print("Valor Final com Imposto: R$", valor_do_produto*(1+taxa_de_imposto/100))

10. Peça ao usuário para inserir o valor total de uma compra e o número de parcelas
desejadas. Calcule e mostre o valor de cada parcela, considerando que não há juros.

valor_total = float(input("Informe o valor total da compra:"))
numero_de_parcelas = int(input("Informe a quantidade de parcelas que deseja:"))
valor_de_parcelas = valor_total/numero_de_parcelas
print("Valor de cada parcela: R$", valor_de_parcelas)"""




