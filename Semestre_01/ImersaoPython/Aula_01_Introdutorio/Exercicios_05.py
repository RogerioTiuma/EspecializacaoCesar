"""5. Escreva um programa que leia o valor total das vendas de um vendedor e a
porcentagem de comissão que ele recebe. Calcule e mostre o valor da comissão."""

valor_total = float(input("Digite o valor total: "))
comissao = float(input("Digite o percentual da comissao: "))
print("Valor da Comissão: ", (valor_total*comissao)/100)
