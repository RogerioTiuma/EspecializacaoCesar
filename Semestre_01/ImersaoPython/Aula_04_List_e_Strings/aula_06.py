notas = []

for i in range(5):
    notas.append(float(input(f"Digite a nota número {i+1}: ")))

media = sum(notas)/len(notas)
print("media: ", media)

for i in notas:
    if i > media:
        print(i)


