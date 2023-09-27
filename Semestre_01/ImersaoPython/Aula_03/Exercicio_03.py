"""3. Uma loja deseja criar um sistema de controle de estoque. O usuário deve inserir o nome
do produto e a quantidade. Se a quantidade for negativa, o programa deve informar um
erro e pedir novamente. Após cada inserção, o sistema solicitará um novo nome ou o
usuário informará “FIM” para encerrar o sistema. Por fim, o sistema deverá apresentar a
quantidade de tipos de produtos inseridos."""

produto = ""
cont_tipos = 0

while produto != "FIM":
    produto = input("Digite o nome do produto: ")

    if produto == "FIM":
        break
    quantidade = int(input("Digite a quantidade do produto: "))

    if quantidade < 0:
        print("Não é possível cadastro de estoque negativo.")
        continue

    cont_tipos += 1

print(f"Tipos de produtos cadastrados: {cont_tipos}")
