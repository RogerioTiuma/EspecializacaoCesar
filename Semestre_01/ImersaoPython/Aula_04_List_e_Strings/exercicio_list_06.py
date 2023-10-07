restaurantes = []
contadores = []
medias = []
restaurante = " "
nota = 0.0
media = 0.0
i = 0

while nota != "PARE":
    restaurante = input("Digite o nome do restaurante: ")
    if restaurante == "PARE":
        break
    nota = int(input(f"Digite a nota do restaurante {restaurante} de 0 à 5 "))

    # testa se o restaurante digitado está na lista restaurantes
    # Se estiver, calcula nova média
    if restaurante in restaurantes:
        i = restaurantes.index(restaurante)
        contadores[i] = contadores[i]+1
        media = ((contadores[i]-1)*medias[i]+nota)/contadores[i]
        medias[i] = media

    # Se o restaurante não estiver listado, agora vai passar a ser
    else:
        restaurantes.append(restaurante)
        medias.append(nota)
        contadores.append(1)

print(f"Restaurante com a maior nota: {restaurantes[medias.index(max(medias))]} - Nota média: {max(medias)}")
print(f"Restaurante com a maior nota: {restaurantes[medias.index(min(medias))]} - Nota média: {min(medias)}")
