"""8. Uma loja deseja oferecer um bônus de natal para seus clientes. O algoritmo deverá
perguntar quantos clientes há na loja, e para cada um deles ler o nome e o valor total das
compras no ano. Se o valor for igual ou maior que R$2.000,00, calcular um bônus de
15% e exibir “Cliente apto para receber o bônus”. Informar ao final quantos clientes
ganharam o bônus e o total em reais.
"""

cliente_bonus = 0
total_bonus = 0

numero_clientes = int(input("Quantos clientes há na loja? "))

for i in range(1, numero_clientes + 1):
    nome_cliente = input(f"Informe o nome do cliente {i}: ")
    valor_compra = float(input(f"Informe o valor total das compras do cliente {nome_cliente} no ano: R$"))

    if valor_compra >= 2000.00:
        bonus = valor_compra * 0.15
        print(f"Cliente apto para receber o bônus")
        cliente_bonus += 1
        total_bonus += bonus

print(f"Clientes: {cliente_bonus}")
print(f"Total: R${total_bonus}")
