"""2. Uma loja online deseja criar um sistema de avaliação de produtos. O usuário deve
inserir uma nota de 1 a 5 para um produto. Se uma nota inválida for digitada o usuário
deverá ser alertado. O programa deve calcular a média das notas. Continue coletando
notas até que o usuário insira -1."""

soma_notas = 0
contador_notas = 0

while True:
    nota = int(input("Digite uma nota de 1 a 5 (-1 para encerrar): "))
    if nota == -1:
        break
    elif nota < 1 or nota > 5:
        print("Nota inválida.")
        continue
    soma_notas += nota
    contador_notas += 1

if contador_notas > 0:
    media = soma_notas / contador_notas
    print(f"Média das notas é: {media}")
else:
    print("Nota inválida")
