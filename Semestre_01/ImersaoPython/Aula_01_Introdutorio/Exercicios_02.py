"""2. Peça ao usuário para inserir o valor original de um produto e a porcentagem de
desconto. Calcule e mostre o valor do produto após o desconto. """

valor_do_produto = int(input("Digite o valor original do produto: "))
desconto = int(input("\nDigite o valor do desconto em porcentagem:"))
print(f"\nValor com desconto: R$ {valor_do_produto*(1-(desconto/100))}")

