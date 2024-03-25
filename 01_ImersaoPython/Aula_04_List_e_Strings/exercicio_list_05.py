numero_de_vendedores = 0
nome = " "
venda = 0.0
nomes = []
vendas = []

i = 0
j = 0

# Determina o número de vendedores
numero_de_vendedores = int(input("Digite o número total de vendedores: "))

# Guarda nomes e vendas
for i in range(numero_de_vendedores):
    nome = input("Informe o nome do vendedor: ")
    venda = float(input("Informe o valor da venda: "))
    nomes.append(nome)
    vendas.append(venda)

# Imprime os valores separando o máximo e mínimo
for j in range(numero_de_vendedores):
    if vendas[j] == max(vendas):
        print(f"{nomes[j]}: {vendas[j]} - Maior volume de vendas!")
    elif vendas[j] == min(vendas):
        print(f"{nomes[j]}: {vendas[j]} - Menor volume de vendas!")
    else:
        print(f"{nomes[j]}: {vendas[j]}")
