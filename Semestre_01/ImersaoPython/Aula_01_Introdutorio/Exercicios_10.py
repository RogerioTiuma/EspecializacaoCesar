"""10. Peça ao usuário para inserir o valor total de uma compra e o número de parcelas
desejadas. Calcule e mostre o valor de cada parcela, considerando que não há juros."""

valor_total = float(input("Informe o valor total da compra:"))
numero_de_parcelas = int(input("Informe a quantidade de parcelas que deseja:"))
valor_de_parcelas = valor_total/numero_de_parcelas
print("Valor de cada parcela: R$", valor_de_parcelas)
