""" 7. Uma academia deseja fazer um censo entre seus clientes para descobrir o mais alto, o
mais baixo, o mais pesado e o mais leve. Antes de iniciar é necessário perguntar ao
usuário quantos clientes há na academia. Após isto, o sistema irá receber, de cada um
dos clientes da academia:
● seu código;
● sua altura;
● e seu peso.

Ao encerrar o programa devem ser informados:
● o código, altura e peso do cliente mais alto
● o código, altura e peso do cliente mais baixo
● o código, altura e peso do cliente mais pesado
● o código, altura e peso do cliente mais leve
● a média das alturas de todos os clientes
● a média dos pesos de todos os clientes
Atenção: Como no exemplo abaixo, o mesmo cliente pode estar dentro de uma ou mais
condições!"""

num_clientes = int(input("Quantos clientes existem: "))

codigo_mais_alto = ""
altura_mais_alto = 0.0
peso_mais_alto = 0.0

codigo_mais_baixo = ""
altura_mais_baixo = 0.0
peso_mais_baixo = 0.0

codigo_mais_pesado = ""
altura_mais_pesado = 0.0
peso_mais_pesado = 0.0

codigo_mais_leve = ""
altura_mais_leve = 0.0
peso_mais_leve = 0.0

soma_alturas = 0
soma_pesos = 0

for i in range(0, num_clientes, 1):
    codigo = input(f"Digite o código do cliente {i + 1}: ")
    altura = float(input(f"Digite a altura do cliente {i + 1}: "))
    peso = int(input(f"Digite o peso do cliente {i + 1}: "))

    if i == 0:
        codigo_mais_alto = codigo
        altura_mais_alto = altura
        peso_mais_alto = peso

        codigo_mais_baixo = codigo
        altura_mais_baixo = altura
        peso_mais_baixo = peso

        codigo_mais_pesado = codigo
        altura_mais_pesado = altura
        peso_mais_pesado = peso

        codigo_mais_leve = codigo
        altura_mais_leve = altura
        peso_mais_leve = peso

    if altura > altura_mais_alto:
        codigo_mais_alto = codigo
        altura_mais_alto = altura
        peso_mais_alto = peso

    if altura < altura_mais_baixo:
        codigo_mais_baixo = codigo
        altura_mais_baixo = altura
        peso_mais_baixo = peso

    if peso > peso_mais_pesado:
        codigo_mais_pesado = codigo
        altura_mais_pesado = altura
        peso_mais_pesado = peso

    if peso < peso_mais_leve:
        codigo_mais_leve = codigo
        altura_mais_leve = altura
        peso_mais_leve = peso

    soma_alturas += altura
    soma_pesos += peso


media_alturas = soma_alturas / num_clientes
media_pesos = soma_pesos / num_clientes

print(f"O cliente mais alto tem: código {codigo_mais_alto}, altura {altura_mais_alto:.2f}m e peso {peso_mais_alto:.1f}kg.")
print(f"O cliente mais baixo tem: código {codigo_mais_baixo}, altura {altura_mais_baixo:.2f}m e peso {peso_mais_baixo:.1f}kg.")
print(f"O cliente mais leve tem: código {codigo_mais_leve}, altura {altura_mais_leve:.2f}m e peso {peso_mais_leve:.1f}kg.")
print(f"O cliente mais pesado tem: código {codigo_mais_pesado}, altura {altura_mais_pesado:.2f}m e peso {peso_mais_pesado:.1f}kg.")
print(f"A média das alturas é: {media_alturas}")
print(f"A média dos pesos é: {media_pesos}")
