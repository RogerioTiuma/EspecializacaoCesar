"""6. Faça um algoritmo que encontre qual o maior número par digitado pelo usuário. O
usuário deve digitar 10 números e ao final o algoritmo deve imprimir o resultado."""

maior_par = 0
primeiro_par = True
for i in range(0, 10, 1):
    numero = int(input("Digite o número: "))
    if numero%2 == 0:
        if primeiro_par:
            maior_par = numero
            primeiro_par = False
        if numero > maior_par:
            maior_par = numero

print(f"Maior número par: {maior_par}")
