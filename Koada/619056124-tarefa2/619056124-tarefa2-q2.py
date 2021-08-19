L1 = []                  #inicia um lista vazia
L = [440.00]             #lista que pretendo somar com a L1 no final
f = 440.00               #inicializando a uma variável que será usada na conta
f1 = 0                   #inicializando uma variável que será usada na conta

for i in range (0,40):   #looping para calcular o valor das frequências da 50° nota à 88° e guarda-las na lista L1
    f1 = f+(2**(1/12))
    f2 = float(f'{f1:.2f}')
    L1 = L1 + [f2]
    f = f1
L1 = L + L1              #Soma das duas listas

f1 = 440.00              #Troco o valor da variável f1
L2 = []                  #Nova lista vazia

for i in range (49,1,-1):   #looping para calcular da 49° nota até a 1°
    f = f1-(2**(1/12))
    f2 = float(f'{f1:.2f}')
    L2 = L2 + [f2]
    f1 = f
L2.pop(0)                   #Excluo o primeiro termo da lista, pois ele já está presente na L1

#Precisamos inverter a ordem da lista, pois ela está decrescente, precisamos colocar em ordem crescente

for f in range (0,len(L2),1):           #Percorre toda a lista L2
    MEN = f                             #HIPOTESE INICIAL
    for i in range(f + 1, len(L2), 1):  #percorrer todos os outros
        if L2[i] < L2[MEN]:
            MEN = i                     #novo campeão
    aux = L2[f]                         #aux é uma variável que vai auxiliar na troca
    L2[f] = L2[MEN]
    L2[MEN] = aux


L3 = L2 + L1                            #Somamos as duas listas

print(L3)

