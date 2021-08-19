#BOAS VINDAS
print("Bem vindo sr.usuario")
#DIÁLOGO DE ENTRADA DE DADOS
#PROCESSAMENTO
arqdados = open("inteiros 20 ord.txt","r")     #associando arquivo externo(inteiros 20.txt ao arqdados)
a=list(map(int,arqdados.readline().split(" ")))
print("vetor lido: \n" , a)
x = int(input("Digite um número para x: "))
print("O número escolhido foi: ",x)
ifs=0                           #contará ifs
atribs=0                        #contará atribuições
a.append (x)                       #pré insiro o x
i=0
ifs=ifs+1
while(a[i]<x):
    i=i+1
    ifs=ifs+1
ifs=ifs+1
if x==a[i]:
    ifs=ifs+1
    if i < len(a)-1:
        print(x," já está no vetor, na posição",i)
        a.pop()                    # retira o x pré inserido
    else:
        print(x,"foi acrescentado no final de a")
else:                           #x é menor que a[i]
    print(x,"deve ser inserido na posição",i)
    for j in range (len(a)-1,i,-1):         # mover bloco para direita
        a[j]=a[j-1]                      # percorre de cima para baixo
        atribs=atribs+1
        a[i] = x                              # insere x
        atribs=atribs+1
print("Após a inserção ficou: \n",a)
print("foram executados", ifs," ifs e", atribs,"atribuições")
#EMISSÃO DE RELATÓRIO DE SAÍDA

#DESPEDIDA

#FINALIZAÇÃO
#