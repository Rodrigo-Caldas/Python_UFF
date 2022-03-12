#P23TRANSP.PY
#UNIVERSIDADE FEDERAL FLUMINENSE
#ESCOLA DE ENGENHARIA
#ENGENHARIA DE RECURSOS HIDRICOS E DO MEIO AMBIENTE
#TCC00326 PROGRAMAÇÃO DE COMPUTADORES - TURMA B1
#SEMESTRE 2020.1
#PROF. JOHN REED
#DATA: 10/11/2020
#NOME: RODRIGO CALDAS MATRÍCULA:
def lematint(arq, l, f):      #Lê matirz de inteiros do arquivo arq com "l" linhas e imprime a frase "f"
    print(f)                  #imprime a frase do usuário
    mat_dados = open(arq, "r")
    mat = []
    for i in range(0, l, 1):           #Percorre as "l" linhas
        mat.append(list(map(int, mat_dados.readline().split(" "))))
    return mat
def impmatint(mat, f):
    print(f)
    for i in range(0, len(mat), 1):
        print(mat[i])
    return

print("Bem-vindo usuário!\n O objetivo é transpor uma matriz quadrada.")
