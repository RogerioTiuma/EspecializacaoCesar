"""3.Dados os lados a, b, e c de um triângulo, calcule sua área."""

a = float(input("Digite o valor do primeiro lado do triângulo:"))
b = float(input("\nDigite o valor do segundo lado do triângulo:"))
c = float(input("\nDigite o valor do terceiro lado do triângulo:"))
s = (a+b+c)/3
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(f"Área do triângulo: {area}")
