tipoDeSecao = input("Informe o tipo de secao (digite 1 para matinê, 2 para vespertina e 3 para noturna): ")
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


"""
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
