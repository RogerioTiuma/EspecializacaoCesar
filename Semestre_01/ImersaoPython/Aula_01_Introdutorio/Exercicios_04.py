"""4.Peça ao usuário para inserir um valor inicial, a taxa de juro e o tempo. Calcule e
mostre o valor futuro após o período especificado com juros simples."""

valor_inicial = float(input("Digite o valor inicial: "))
taxa_de_juros = float(input("Digite a taxa de juros: "))
tempo = float(input("Digite o tempo de parcelamento: "))
print("O valor futuro: ", (valor_inicial+(valor_inicial*taxa_de_juros*tempo)/100))
