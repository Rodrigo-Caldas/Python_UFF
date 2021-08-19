#DESCRIÇÃO DE OBJETOS DO PROGRAMA
def achamen(vet,p):    #vet: vetor onde buscará; P: ponto inicial da busca
    men=0             #Hipótese inicial
    for j in range(1,p+1,1):           #Percorre todos os outros, corrigindo a hipótese.
        if vet[j]<vet[men]:      #se surgir um candidato melhor...
            men=j            #...temos um novo campeão.
    return (men)               #retorna a posição do menor do vetor a partir da posição P
#BOAS VINDAS
print("Seja bem vindo, senhor usuário.")
#DIÁLOGO DE ENTRADA DE DADOS
arq_dados=open("INTEIROS 20", "r")        #associando INTEIROS 20 ao arq_dados
a=list(map(int,arq_dados.readline().split(" ")))
print("O vetor lido foi: \n", a)
#PROCESSAMENTO
for f in range(len(a)-1, 0, -1):           #percorre o vetor decrescentemente ordenando a posição f
    men = achamen(a,f)                      #Localiza o menor
    aux=a[f]
    a[f]=a[men]                       #Põe no lugar
    a[men]=aux
    print(a)
#EMISSÃO DE RELATÓRIO DE SAÍDA
print("Após a ordenação, o vetor ficou:\n", a)
#DESPEDIDA
print("Fim do progama, obrigado por utilizar.")
#FINALIZAÇÃO
#   <comandos para o encerramento do programa, se houver>