import model


alunos = {}


def printar_dicionario():
    print(alunos)
def criar(nome_aluno, nome_mae, ano_nascimento, serie):

    model.id = 0
    model.matricula += 1
    model.nome_aluno = nome_aluno
    model.nome_mae = nome_mae
    model.ano_nascimento = ano_nascimento
    model.serie = serie
    alunos[model.matricula] = [model.nome_aluno,model.nome_mae,model.ano_nascimento,model.serie]
    print(alunos)

def atualizar(matricula,nome_aluno="", nome_mae="", ano_nascimento=0, serie=0):
    if nome_aluno != "":
        alunos[matricula][0] =nome_aluno
    if nome_mae != "":
        alunos[matricula][1] = nome_mae
    if ano_nascimento != 0:
        alunos[matricula][2] = ano_nascimento
    if serie != 0:
        alunos[matricula][3] = serie


def consultar(matricula):
    print(alunos[matricula])

def excluitr(matricula):
    del alunos[matricula]