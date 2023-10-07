"""No Hospital Todos Juntos, a escala de plantão dos técnicos em enfermagem, para o mês de novembro, está sendo definida. Há 30 técnicos. Faça um programa que armazene o nome e o dia de trabalho (1 a 30) de cada técnico. Caso o usuário digite um dia inválido, deverá permanecer no loop até digitar um dia entre 1 e 30. Por fim, separe em duas tuplas que terão os nomes e os dias de trabalhos dos funcionários. Uma tupla constará os funcionários que irão trabalhar em dia par e a outra os funcionários que irão trabalhar em dia ímpar.
Atenção: o primeiro index de cada tupla será o nome e o segundo index será o dia de trabalho. As duas tuplas juntas devem conter informações sobre os 30 técnicos."""
nomes = []
dias = []
nomes_pares = []
nomes_impares = []
dias_pares = []
dias_impares = []
plantao_par = ()
plantao_impar = ()
i = 0
j = 0
tam = 5

for i in range(tam):
    nome = input("Digite o nome do técnico: ")
    dia = int(input("Digite o dia do plantão, valor entre 1 e 30: "))
    while (dia < 1) or (dia > 30):
        dia = int(input("Dia inválido! Digite um dia entre 1 e 30: "))
    nomes.append(nome)
    dias.append(dia)

for j in range(tam):
    if dias[j] % 2 == 0:
        nomes_pares.append(nomes[j])
        dias_pares.append(dias[j])
    else:
        nomes_impares.append(nomes[j])
        dias_impares.append(dias[j])

plantao_par = (nomes_pares, dias_pares)
plantao_impar = (nomes_impares, dias_impares)

print("Pessoas no plantão (dias pares): ", plantao_par)
print("Pessoas no plantão (dias impares): ", plantao_impar)
