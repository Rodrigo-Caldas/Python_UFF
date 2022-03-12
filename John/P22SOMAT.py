#P22SOMAT.PY
#UNIVERSIDADE FEDERAL FLUMINENSE
#ESCOLA DE ENGENHARIA
#ENGENHARIA DE RECURSOS HIDRICOS E DO MEIO AMBIENTE
#TCC00326 PROGRAMAÇÃO DE COMPUTADORES - TURMA B1
#SEMESTRE 2020.1
#PROF. JOHN REED
#DATA: 10/11/2020
#NOME: Rodrigo Caldas MATRÍCULA:
#P22SOMAT.PY: SOMA DUAS MATRIZES
#-------------------------------------------------
#DESCRIÇÃO DOS OBJETOS DO PROGRAMA
# <descrição dos objetos e métodos>
#BOAS VINDAS
print("BEM VINDO SR USUÁRIO!")
print("O P22SOMAT.PY SOMA DUAS MATRIZES")
print(" ")
#DIÁLOGO DE ENTRADA DE DADOS
mat_dados = open("MATINT34.txt","r")
A = []                        #matriz incialmente vazia
for i in range(0,3,1):             #percorre as três linhas
    A.append(list(map(int,mat_dados.readline().split(" "))))
print("MATRIZ LIDA: (3 linhas e", len(A[0]),"colunas)")
for i in range(0,3,1):
    print(A[i])
mat_dados = open("MATINT-2.txt","r")
B = []                        #matriz incialmente vazia
for i in range(0,3,1):             #percorre as três linhas
    B.append( list(map(int,mat_dados.readline().split(" "))))
print("MATRIZ LIDA: (3 linhas e", len(B[0]),"colunas)")
for i in range(0,3,1):
    print(B[i])
print("SOMANDO AS MATRIZES A E B")
C = []
for i in range(0,len(A),1):     #percorro as linhas
    L = []                      #linha temporária
    for j in range(0,len(A[i]),1):  #percorro as colunas desta linha
        L.append(A[i][j]+B[i][j])   #acrescenta mais um elemento na linha temporária
    C.append(L)                     #acrescenta nova linha em C
print("MATRIZ C CALCULADA: (3 linhas e", len(C[0]),"colunas)")
for i in range(0,3,1):
    print(C[i])
print(" ")
#PROCESSAMENTO
#--------------------------------------------
#EMISSÃO DE RELATÓRIO DE SAÍDA
#--------------------------------------------
#DESPEDIDA
print("AGRADECEMOS PELA UTILIZAÇÃO DO PROGRAMA!")
#FINALIZAÇÃO
print("PROGRAMA OPERADO COM SUCESSO!")