"""10. Um matemático deseja explorar variações da famosa sequência de Fibonacci. Em vez de
começar com os números 0 e 1, ele quer começar com dois números quaisquer e gerar a
sequência a partir deles. O usuário deve inserir os dois primeiros números da sequência.
Em seguida, o programa deve gerar os próximos 20 números da sequência, onde cada
número é a soma dos dois anteriores, assim como na sequência de Fibonacci tradicional.
Ao final, o programa deve exibir a sequência completa de 22 números."""

numero_1 = int(input("Informe o primeiro número para a sequência de Fibonacci"))
numero_2 = int(input("Informe o segundo número para a sequência de Fibonacci"))
i = 0
while numero_2 <= numero_1:
    numero_2 = input("O segundo número é inválido. Digite novamente. Informe o segundo número para a sequência de Fibonacci")

print("")
print("Sequência:")
print(numero_1)
print(numero_2)

for i in range(i, 20, 1):
    print(numero_1+numero_2)
    auxiliar = numero_1
    numero_1 = numero_2
    numero_2 = auxiliar+numero_2
