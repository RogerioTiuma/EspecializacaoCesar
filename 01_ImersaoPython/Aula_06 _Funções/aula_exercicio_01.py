def conversor(horas):
    return horas*60


# Programa principal

h = int(input("Digite uma hora: "))
m = conversor(h)

print(f"{h} horas em minutos é {m}.")
