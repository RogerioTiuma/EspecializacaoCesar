"""4. Um petshop atende 10 cachorros por tarde. Faça um programa que solicite ao usuário o
código do serviço efetuado: (1 - banho; 2 - tosa; 3 - banho e tosa; 4- outros). Por fim,
exiba a quantidade de solicitações para cada um deles.
"""
banho = 0
tosa = 0
banho_tosa = 0
outros = 0

for i in range(0, 10, 1):
    codigo = int(input("Digite o código do serviço 1 - banho; 2 - tosa; 3 - banho e tosa; 4- outros: "))
    if codigo == 1:
        banho += 1
    elif codigo == 2:
        tosa += 1
    elif codigo == 3:
        banho_tosa += 1
    elif codigo == 4:
        outros += 1

print(f"Banho: {banho}")
print(f"Tosa: {tosa}")
print(f"Banho e tosa: {banho_tosa}")
print(f"Outros: {outros}")
