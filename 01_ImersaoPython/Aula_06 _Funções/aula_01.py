def bom_dia(n,i):
    print("Olá, bom dia")
    print(f"Bem-vindo(a),  {n}")
    print(f"Você tem {i} anos.")


# Programa principal
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
bom_dia(nome, idade)
