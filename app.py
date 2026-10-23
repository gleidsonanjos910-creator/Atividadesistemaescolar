
from aluno import Aluno
from utils.io import *

def exibirMenu():
    menu = """
SISTEMA ACADEMIA
-------------------------
1: cadastrar aluno
2: listar alunos
3: filtrar por IMC
0: sair
"""
    print(menu)


def print_alunos(alunos, imc=0):
    print(f"Relação de alunos com IMC a partir de {imc}:")

    encontrou = False

    for aln in alunos:
        if aln.imc >= imc:
            print(aln)
            encontrou = True

    if not encontrou:
        print("Nenhum aluno encontrado.")


alunos = []
proximo_id = 1

while True:
    exibirMenu()
    opc = ler_inteiro("Opção: ", positivo=True)

    if opc == 0:
        print("Sistema encerrado.")
        break

    elif opc == 1:
        aln = Aluno(id=proximo_id)
        proximo_id += 1
        aln.ler_dados()
        alunos.append(aln)

        print("Cadastro efetuado com sucesso!")
        print(aln)
        limpar_tela()

    elif opc == 2:
        print_alunos(alunos)
        limpar_tela()

    elif opc == 3:
        filtro = ler_decimal(
            "Filtrar IMC a partir de: ",
            positivo=True
        )
        print_alunos(alunos, imc=filtro)
        limpar_tela()

    else:
        print("Opção inválida!")
