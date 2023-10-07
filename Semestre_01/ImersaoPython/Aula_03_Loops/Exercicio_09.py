"""9. Uma grande rede de lojas deseja analisar o desempenho de vendas de seus produtos ao
longo de um ano. Para isso, eles coletaram os valores de vendas mensais de um
determinado produto durante os 12 meses do ano. O sistema deve permitir que o usuário
insira os valores de vendas para cada mês, começando por janeiro e terminando em
dezembro. Após a inserção, o programa deve calcular:
● O mês com a maior venda.
● O mês com a menor venda.
● A média de vendas ao longo do ano.
● O total de vendas no ano.

menor_venda = 0
maior_venda = 0
soma_venda = 0
mes_de_maior_venda = ""
mes_de_menor_venda = "" """

for i in ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Junho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]:
    venda_do_mes_atual = int(input(f"Digite a venda do mês de {i}"))

    if i == "Janeiro":
        mes_de_menor_venda = i
        menor_venda = venda_do_mes_atual
        mes_de_maior_venda = i
        maior_venda = venda_do_mes_atual

    elif menor_venda > venda_do_mes_atual:
        menor_venda = venda_do_mes_atual
        mes_de_menor_venda = i

    elif maior_venda < venda_do_mes_atual:
        maior_venda = venda_do_mes_atual
        mes_de_maior_venda = i

    soma_venda += venda_do_mes_atual

print("")
print(f"Mês com a maior venda: {mes_de_maior_venda} (R$ {maior_venda})")
print(f"Mês com a menor venda: {mes_de_menor_venda} (R$ {menor_venda})")
print("Média de vendas ao longo do ano: R$ ", soma_venda/12)
print("Total de vendas no ano: R$ ", soma_venda)
