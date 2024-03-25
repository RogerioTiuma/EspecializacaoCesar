from pessoa import idade_func, votar


# idade = pessoa.idade_func() Só precisa usar .pessoa se não usar o import para as funções que você quer (ex.: pessoa)
idade = idade_func()
print(f"Sua idade é {idade} ")

"""
pode_votar = pessoa.votar(idade)
if pode_votar: 
    print("Pode votar.")
else:
    print("Não pode votar.")"""
