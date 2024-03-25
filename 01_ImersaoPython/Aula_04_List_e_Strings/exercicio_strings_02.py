"""2. Faça um programa que peça ao usuário para inserir:
○ uma frase
○ uma palavra que está contida na frase
○ outra palavra que ele deseja substituir no lugar da primeira palavra inserida. Por fim, o programa exibe a frase modificada, toda em letra maiúscula."""

frase = input("Digite uma frase: ")
busca = input("Digite uma palavra para buscar na frase: ")
substituta = input("Digite uma palavra para substituir a palavra a ser buscada: ")

frase2 = frase.replace(busca, substituta)

print(frase2)
