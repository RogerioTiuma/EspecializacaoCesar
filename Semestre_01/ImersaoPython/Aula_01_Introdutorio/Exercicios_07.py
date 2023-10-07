"""7. Escreva um programa que leia o custo de produção de um produto e seu preço de
venda. Calcule e mostre o lucro bruto obtido na venda do produto."""

custo_de_producao = int(input("Qual o valor do custo de produção? "))
lucro_bruto = int(input("Qual o valor do lucro bruto? "))
print("Lucro Bruto: R$", lucro_bruto-custo_de_producao)
