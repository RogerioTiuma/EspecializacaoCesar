"""tipoDeSecao = input("Informe o tipo de secao (digite 1 para matinê, 2 para vespertina e 3 para noturna): ")
idade = int(input("Informe sua idade: "))
estudante = input("Você é estudante, meu camarada?")

if tipoDeSecao == "1":
    if(idade <= 12) or (idade >= 65):
        print("Valor do ingresso: R$ ", 20*0.5)
    elif estudante == "S":
        print("Valor do ingresso: R$ ", 20*0.5)
    else:
        print("Valor do ingresso: R$ ", 20)
if tipoDeSecao == "2":
    if(idade <= 12) or (idade >= 65):
        print("Valor do ingresso: R$ ", 25*0.5)
    elif estudante == "S":
        print("Valor do ingresso: R$ ", 25*0.5)
    else:
        print("Valor do ingresso: R$ ", 25)

if tipoDeSecao == "3":
    if(idade <= 12) or (idade >= 65):
        print("Valor do ingresso: R$ ", 30*0.5)
    elif estudante == "S":
        print("Valor do ingresso: R$ ", 30*0.5)
    else:
        print("Valor do ingresso: R$ ", 30)



suite = input("Informe o tipo de suite (digite 1 para standard, 2 para luxo e 3 para presidencial): ")
numero_de_noites = int(input("Informe o número de noites que deseja: "))

if suite == "1":
    if (numero_de_noites >= 5) and (numero_de_noites <= 15):
        print("Valor total da estadia: R$ ", numero_de_noites*250*0.9)
    elif (numero_de_noites < 5) and (numero_de_noites >= 1):
        print("Valor total da estadia: R$ ", numero_de_noites*250)
    else:
        print("Limite de noites atingido.")

if suite == "2":
    if (numero_de_noites >= 5) and (numero_de_noites <= 10):
        print("Valor total da estadia: R$ ", numero_de_noites*500*0.9)
    elif (numero_de_noites < 5) and (numero_de_noites >= 1):
        print("Valor total da estadia: R$ ", numero_de_noites*500)
    else:
        print("Limite de noites atingido.")

if suite == "3":
    if (numero_de_noites >= 5) and (numero_de_noites <= 7):
        print("Valor total da estadia: R$ ", numero_de_noites*1200*0.9)
    elif (numero_de_noites < 5) and (numero_de_noites >= 1):
        print("Valor total da estadia: R$ ", numero_de_noites*1200)
    else:
        print("Limite de noites atingido.")"""

tipo_de_franquia = input("Informe o tipo de franquia (Básico, Intermediário ou Avançado):")
franquia_de_minutos = int(input("Informe a quantidade de minutos usada: "))
franquia_de_internet = int(input("Informe a quantidade de internet usada: "))
excedente_minutos = 0
excedente_GB = 0


if tipo_de_franquia == "Básico":
    if franquia_de_minutos > 100:
        excedente_minutos = franquia_de_minutos-100
    if franquia_de_internet > 5:
        excedente_GB = franquia_de_internet-5
    print("Valor da fatura: R$", 50+excedente_GB+excedente_minutos)

if tipo_de_franquia == "Intermediário":
    if franquia_de_minutos > 300:
        excedente_minutos = franquia_de_minutos-300
    if franquia_de_internet > 10:
        excedente_GB = franquia_de_internet-10
    print("Valor da fatura: R$", 80+excedente_GB+excedente_minutos)

if tipo_de_franquia == "Avançado":
    if franquia_de_minutos > 500:
        excedente_minutos = franquia_de_minutos-500
    if franquia_de_internet > 20:
        excedente_GB = franquia_de_internet-20
    print("Valor da fatura: R$", 120+excedente_GB+excedente_minutos)

