# P24MUMAT.PY.PY
# UNIVERSIDADE FEDERAL FLUMINENSE
# ESCOLA DE ENGENHARIA
# ENGENHARIA MECÂNICA
# TCC00326 PROGRAMAÇÃO DE COMPUTADORES - TURMA B1
# SEMESTRE 2020.1
# PROF. JOHN REED
# DATA: 17/11/2020
# NOME: LUCAS SANTANA MATEUS     MATRÍCULA: 119040017
# P24MUMAT.PY.PY: MULTIPLICA DUAS MATRIZES LIDAS DE ARQUIVO
#-------------------------------------------------
# DESCRIÇÃO DOS OBJETOS DO PROGRAMA
def lematint(arq, l,f):         # LÊ MATRIZ DE INTEIROS DO ARQUIVO arq COM l LINHAS E IMPRIME A FRASE f
    print(f)                    # IMPRIME A FRASE DO USUÁRIO
    mat_dados = open(arq, "r")  # ASSOCIA O NOME INTERNO AO NOME EXTERNO
    mat = []                    # MATRIZ VAZIA
    for i in range(0, l, 1):    # PERCORRE AS l LINHAS
        mat.append(list(map(int, mat_dados.readline().split(" ")))) # PREENCHENDO A MATRIZ mat
    return mat
def impmatint(mat, h, f):   # IMPRIME A MATRIZ mat EM CAMPOS DE LARGURA h E A FRASE f
    print(f)                # IMPRIME A FRASE DO USUÁRIO
    for i in range(0, len(mat), 1):  # PERCORRE AS LINHAS DA MATRIZ
        for j in range(0,len(mat[i]),1):
             print((repr(mat[i][j]).rjust(h)), sep='', end='') # FUNÇÃO PYTHON
        print()
    return
def mumat(ma,mb):   # MULTIPLICA A MATRIZ ma PELA MATRIZ mb
    mc=[]           # MATRIZ C COMEÇA VAZIA
    if(len(ma[0])==len(mb)):   # TESTA COMPATIBILIDADE (COLUNAS DE A IGUAL A LINHAS B)
        for i in range(0,len(ma),1):   # PERCORRE LINHAS DE C (IGUAL LINHAS DE A)
            L = []
            for j in range(0,len(mb[0]),1):      # PERCORRE COLUNAS DE C (IGUAL COLUNAS B)
                s = 0      # ACUMULA OS PRODUTOS
                for k in range(0,len(ma[0])):    # PERCORRE COLUNAS DE A (E LINHAS DE B)
                    s = s + ma[i][k] * mb[k][j]  # ACUMULA NOVO PRODUTO
                L.append(s)  # ACRESCENTA UM NOVO ELEMENTO A LINHA DE C
            mc.append(L)     # ACRESCENTA NOVA LINHA A C
        codigo=0
    else:
        codigo=1    # MATRIZES DE DIMENSÕES INCOMPATÍVEIS
    return(mc,codigo)
# BOAS VINDAS
print("BEM VINDO SR.USUÁRIO")
print("P24MUMAT.PY MULTIPLICA DUAS MATRIZES LIDAS DE ARQUIVO")
print(" ")
# DIÁLOGO DE ENTRADA DE DADOS
A = lematint("MAT3X4.txt", 3, "LENDO A MATRIZ DO ARQUIVO MAT3X4.txt: ")
impmatint(A, 3, "MATRIZ A LIDA: ")
print(" ")
B = lematint("MAT4X2.txt", 4, "LENDO A MATRIZ DO ARQUIVO MAT4X2.txt: ")
impmatint(B, 3, "MATRIZ B LIDA: ")
# PROCESSAMENTO
# CHAMADA DA MUMAT
(C,cod) = mumat(A,B)
# EMISSÃO DE RELATÓRIO DE SAÍDA
print(" ")
impmatint(C, 5, "MATRIZ C (RESULTADO DE A * B)")
# DESPEDIDA
print("--------------------------------")
print("OBRIGADO POR UTILIZAR O PROGRAMA")
# FINALIZAÇÃO
print("\nPROCEDIMENTO ENCERRADO")
