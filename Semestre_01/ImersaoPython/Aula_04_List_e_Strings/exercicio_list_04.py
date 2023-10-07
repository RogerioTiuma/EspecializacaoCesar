""" 4. Faça um programa que:

○ Receba a temperatura média de cada mês do ano e armazene-as em uma lista.
○ Calcule a média anual de temperaturas
○ Exiba todos os meses que têm as temperaturas acima da média anual (mostrar o
mês por extenso: Janeiro, Fevereiro, . . . ). Dica: Crie uma lista de strings com
todos os nomes dos meses."""

i = 0
j = 0
t = 0
soma = 0.0
media = 0.0
temperatura = 0.0
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []

# Atribuir temperaturas
for i in range(12):
    temperatura = float(input(f"Digite o valor da temperatura média do mês {meses[i]}: "))
    temperaturas.append(temperatura)

# Calcular Média
for t in range(12):
    soma += temperaturas[t]
media = soma/12
print("Média Anual de Temperatura: ", media)

# Exibir Meses Acima da Média
print("Meses com temperaturas acima da média: ")
for j in range(12):
    if temperaturas[j] > media:
        print(meses[j])
