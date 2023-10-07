"""3. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário como
String. Usando manipulação de Strings, altere a frase e exiba como no exemplo."""

# Solicita entrada
data = input("Digite a data do seu nascimento no formato dd/mm/aaaa: ")
# Separa a data
data2 = data.split("/")
# Imprime o resultado
meses_escritos = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
print(f"Você nasceu em {data2[0]} de {meses_escritos[int(data2[1])-1]} de {data2[2]}.")
