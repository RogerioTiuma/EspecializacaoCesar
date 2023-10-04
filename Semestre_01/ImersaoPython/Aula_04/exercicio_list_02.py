"""2. Faça um programa que:
○ Peça duas notas de 5 estudantes.
○ Calcule e armazene numa lista a média de cada estudante.
○ Imprima a lista de médias;
○ Imprima o número de estudantes com média >= 7.0."""

nota_01 = 0.0
nota_02 = 0.0
count = 0
i = 0
j = 0
medias = []

# Coleta as notas e guarda as médias
for i in range(5):
    nota_01 = float(input(f"Digite a nota 1 do estudante {i+1} "))
    nota_02 = float(input(f"Digite a nota 2 do estudante {i+1} "))
    medias.append((nota_01+nota_02)/2)

# Conta médias superiores a 7
for j in medias:
    if j >= 7:
        count += 1

print("Médias: ", medias)
print("Número de estudantes com média >= 7:", count)
