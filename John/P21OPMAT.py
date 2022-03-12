#P21OPMAT.PY
#UNIVERSIDADE FEDERAL FLUMINENSE
#ESCOLA DE ENGENHARIA
#ENGENHARIA DE RECURSOS HIDRICOS E DO MEIO AMBIENTE
#TCC00326 PROGRAMAÇÃO DE COMPUTADORES - TURMA B1
#SEMESTRE 2020.1
#PROF. JOHN REED
#DATA: 10/11/2020
#NOME: RODRIGO CALDAS MATRÍCULA:
#P21OPMAT.PY: APRESENTA OPERAÇÕES BÁSICAS SOBRE MATRIZES
#-------------------------------------------------
#DESCRIÇÃO DOS OBJETOS DO PROGRAMA
# <descrição dos objetos e métodos>
#BOAS VINDAS
print("BEM VINDO SR USUÁRIO!")
print("O P21OPMAT.PY APRESENTA OPERAÇÕES BÁSICAS SOBRE MATRIZES")
print(" ")
#DIÁLOGO DE ENTRADA DE DADOS
mat_dados = open("MATINT34.txt","r")
mat3x4 = []                        #matriz incialmente vazia
for i in range(0,3,1):             #percorre as três linhas
    mat3x4.append( list(map(int,mat_dados.readline().split(" "))))
print("MATRIZ LIDA: (3 linhas e", len(mat3x4[0]),"colunas)")
for i in range(0,3,1):
    print(mat3x4[i])
print("MULTIPLICANDO UMA LINHA POR UMA CONSTANTE")
i = int(input("INFORME A LINHA DESEJADA A SER MULTIPLICADA: "))
k = int(input("INFORME A CONSTANTE A SER MULTIPLICADA: "))
for j in range(0,len(mat3x4[0]),1):         #percorro as colunas da linha i
    mat3x4[i][j] = mat3x4[i][j]*k
print("APÓS A MULTIPLICAÇÃO FICOU: ")
for i in range(0,3,1):
    print(mat3x4[i])
print("SOMANDO DUAS LINHAS")
i = int(input("INFORME A LINHA A SER MODIFICADA: "))
j = int(input("INFORME A LINHA A SER ACRESCIDA NA PRIMEIRA: "))
for k in range(0,len(mat3x4[0]),1):           #percorro as colunas da linha i
    mat3x4[i][k]=mat3x4[i][k]+ mat3x4[j][k]
print("APÓS A SOMA DE LINHAS FICOU: ")
for i in range(0,3,1):
    print(mat3x4[i])
print("TROCANDO DUAS LINHAS DE POSIÇÃO")
i = int(input("INFORME A LINHA A SER TROCADA: "))
j = int(input("INFORME A OUTRA LINHA A SER TROCADA: "))
for k in range(0,len(mat3x4[0]),1):
    aux = mat3x4[i][k]
    mat3x4[i][k] = mat3x4[j][k]
    mat3x4[j][k] = aux
print("APÓS A TROCA DE LINHAS FICOU: ")
for i in range(0,3,1):
    print(mat3x4[i])
print(" ")
#PROCESSAMENTO
#-------------------------------------------
#EMISSÃO DE RELATÓRIO DE SAÍDA
#-------------------------------------------
#DESPEDIDA
print("AGRADEÇEMOS PELOS VALORES INFORMADOS")
print(" ")
#FINALIZAÇÃO
print("PROGRAMA OPERADO COM SUCESSO")