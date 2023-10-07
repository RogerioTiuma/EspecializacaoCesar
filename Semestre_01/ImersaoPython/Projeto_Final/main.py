import service
import model

opcao = 0

service.criar("Luis", "maria", 1990, 5)
service.criar("Marcos", "Josefina", 1991, 5)
"""service.atualizar(2,nome_mae="Carla")
service.printar_dicionario()
service.consultar(1)
service.excluitr(1)
service.printar_dicionario()"""


while True:
    if opcao == 5:
        break
    print("1 - Criar matricula. Digite 5 para parar.")
    print("2 - Editar matricula. Digite 5 para parar.")
    print("3 - Consultar matricula. Digite 5 para parar.")
    print("4 - Excluir matricula. Digite 5 para parar.")

    opcao = int(input("Digite um número para definir a ação: "))

    if opcao == 1:
        nome_aluno = input("Digite o nome do aluno: ")
        ano_nascimento = int(input("Digite a data de "))
        nome_mae = input("Digite o nome da mãe do aluno: ")
        serie = int(input("Digite a série do aluno"))
        service.criar(nome_aluno, ano_nascimento, nome_mae, serie)

    elif opcao == 2:
        matricula = int(input("Digite a matricula do aluno: "))
        nome_aluno = input("Digite o nome do aluno: ")
        ano_nascimento = int(input("Digite a data de "))
        nome_mae = input("Digite o nome da mãe do aluno: ")
        serie = int(input("Digite a série do aluno"))
        service.atualizar(matricula, nome_aluno, ano_nascimento, nome_mae, serie)

    elif opcao == 3:
        matricula = int(input("Digite a matricula do aluno à ser consultado: "))
        service.consultar(matricula)

    elif opcao == 4:
        matricula = int(input("Digite a matricula do aluno à ser excluído: "))
        service.excluitr(matricula)

    else:
        opcao == 5
