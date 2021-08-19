#P25TRIANGAUSS.PY
#UNIVERSIDADE FEDERAL FLUMINENSE
#ESCOLA DE ENGENHARIA
#ENGENHARIA DE RECURSOS HÍDRICOS E DO MEIO AMBIENTE
#TCC00326 PROGRAMAÇÃO DE COMPUTADORES - TURMA B1
#SEMESTRE 2020.1
#PROF. JOHN REED
#DATA: 19/11/2020
#NOME: JOÃO VICTOR BASILIO MARTINS MATRÍCULA: 218056089
#P25TRIANGAUSS.PY: TRIANGULARIZA UMA MATRIZ POR GAUSS
#-------------------------------------------------
#DESCRIÇÃO DOS OBJETOS DO PROGRAMA
def lematfloat(arq,l,f):              #lê a matriz de REAIS do arquivo arq com l linhas e imprime f
    print(f)                          #imprime a matriz
    mat_dados = open(arq,"r")         #associa o nome interno ou externo
    mat = []                          #matriz vazia
    for i in range(0,l,1):            #percorre as linhas da matriz
        mat.append(list(map(float,mat_dados.readline().split(" "))))
    return (mat)
def impmatfor(mat, fmt, f):   # IMPRIME A MATRIZ mat EM CAMPOS DE FORMATO fmt E A FRASE f
    print(f)             # IMPRIME A FRASE DO USUÁRIO
    for i in range(0, len(mat), 1): # PERCORRE AS LINHAS DA MATRIZ
        for j in range(0,len(mat[i]),1):
             print(("{:" + fmt + "}").format(mat[i][j]), end="")  # IMPRIME FORMATADO
        print()
    return
#BOAS VINDAS
print("BEM VINDO SR. USUÁRIO!")
print("O PROGRAMA P25TRIANGAUSS.PY REALIZA A TRIANGULARIZAÇÃO DE UMA MATRIZ PELO MÉTODO DE GAUSS")
print(" ")
#DIÁLOGO DE ENTRADA DE DADOS
a = lematfloat("MAT4X5.txt",4, "LENDO A MATRIZ DE REAIS DO ARQUIVO MAT4X5.txt...")
impmatfor(a,"10.5f","MATRIZ a LIDA: ")
#PROCESSAMENTO
#MÉTODO DE GAUSS:
for j in range(0,len(a[0])-1,1):        #percorro as colunas da matriz
    #condensação pivotal
    m = j             #hipótese inicial
    for i in range(j,len(a),1):
        if (abs(a[i][j])>(abs(a[m][j]))):    #se aparecer um melhor...
            m = i      #temos um novo campeão
    if m != j:
        for k in range(j,len(a[j]),1):
            aux = a[j][k]
            a[j][k] = a[m][k]
            a[m][k] = aux
        print(" ")
        print("CONDENSAÇÃO PIVOTAL")
        print(" ")
    if a[m][j] == 0:
        print("SISTEMA IMPOSSÍVEL!")
    else:
        for k in range(len(a[j])-1,j-1,-1):    #divindo a linha J por a(j,j)
            a[j][k] =  a[j][k]/ a[j][j]
        for i in range(j+1,len(a),1):       #percorre linhas abaixo da linha j
            for k in range(j,len(a[j]),1):        #percorre as colunas da linha i
                a[i][k] = a[i][k] - a[i][j]*a[j][k]
#EMISSÃO DE RELATÓRIO DE SAÍDA
impmatfor(a,"10.5f","MATRIZ TRIANGULARIZADA: ")
print(" ")
#DESPEDIDA
print("AGRADECEMOS PELA UTILIZAÇÃO DO PROGRAMA!")
print(" ")
#FINALIZAÇÃO
print("PROGRAMA OPERADO COM SUCESSO!")