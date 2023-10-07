"""9. Peça ao usuário para inserir o valor de um produto e a taxa de imposto aplicada sobre
ele. Calcule e mostre o valor final do produto com o imposto."""

valor_do_produto = float(input("Informe o valor do produto:"))
taxa_de_imposto = float(input("Informe a taxa: "))
print("Valor Final com Imposto: R$", valor_do_produto*(1+taxa_de_imposto/100))
