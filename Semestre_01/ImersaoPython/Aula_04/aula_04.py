notas = [6.0, 8.5, 4.5, 10.0, 9.5]

print("A menor nota foi: ", min(notas))
print("A maior nota foi: ", max(notas))
print("A soma das notas foi: ", sum(notas))
print("A média das notas foi: ", sum(notas)/len(notas))

# Insere algo na posição final
notas.append(7.6)

# Insere em uma posição específica
notas.insert(2, 8.4)
print(notas)

# verifica a posição de algum valor na lista
print(notas.index(8.5))
print("aqui")

# Remove o último da lista
notas.pop()
print(notas)

# Remove valor da posição 2
notas.pop()
print(notas)

# Remove um valor específico
notas.remove(10)
print(notas)

# Ordena de forma crescente ou alfabética
notas.sort()
print(notas)

# Ordena de forma decrescente
notas.reverse()
print(notas)
