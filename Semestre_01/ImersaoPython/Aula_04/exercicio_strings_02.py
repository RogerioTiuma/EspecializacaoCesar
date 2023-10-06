frase = input("Digite uma frase: ")
busca = input("Digite uma palavra para buscar na frase: ")
substituta = input("Digite uma palavra para substituir a palavra a ser buscada: ")

frase2 = frase.replace(busca, substituta)

print(frase2)