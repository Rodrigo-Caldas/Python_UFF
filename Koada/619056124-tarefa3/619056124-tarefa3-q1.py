base = input("Digite uma cadeia de bases nitrogenadas: ")
lista1 = list(base)
lista = []

for i in range (0, len(lista1)):
    lista = lista + [lista1[i]]


#Loop para trocar as letras da cadeia de bases nitrogenadas e obter a cadeia complementar
for i in range(0,len(lista1)):
    if lista1[i] == 'A':
        lista1[i] = 'T'
    elif lista1[i] == 'T':
        lista1[i] = 'A'
    elif lista1[i] == 'C':
        lista1[i] = 'G'
    elif lista1[i] == 'G':
        lista1[i] = 'C'
#print(lista1)

#Função para inverter a ordem da cadeia de bases nitrogenadas
lista1.reverse()
#print(lista1)

#Uso a função join na minha lista1, assim ela será transformada em uma string e será guardada na variável base2
base2 = "".join(lista1)
print(base2)

#Uso a função count para contar a quantidade de cada base nitrogenada presente na cadeia
A = base.count('A')
#print(A)
T = base.count('T')
#print(T)
C = base.count('C')
#print(C)
G = base.count('G')
#print(G)

#Teste para saber qual é a base nitrogenada mais frequente na cadeia, caso tenham bases com frequências iguais a que obteve maior frequência primeiro é mostrada na saída
a = 0
t = 0
g = 0
c = 0
venceA = 0
venceT = 0
venceC = 0
venceG = 0

countA = 0
countT = 0
countC = 0
countG = 0

for i in range (0, len(lista)):
    if lista[i] == 'A':
        a = a + 1
        t = 0
        g = 0
        c = 0
        if venceA < a:
            venceA = a
            countA = i
    if lista[i] == 'T':
        t = t + 1
        a = 0
        g = 0
        c = 0
        if venceT < t:
            venceT = t
            countT = i
    if lista[i] == 'G':
        g = g + 1
        t = 0
        a = 0
        c = 0
        if venceG < g:
            venceG = g
            countG = i
    if lista[i] == 'C':
        c = c + 1
        a = 0
        t = 0
        g = 0
        if venceC < c:
            venceC = c
            countC = i

if venceA>venceT and venceA>venceG and venceA>venceC:
    print(venceA*'A')
elif venceT>venceA and venceT>venceG and venceT>venceC:
    print(venceT*'T')
elif venceC>venceT and venceC>venceG and venceC>venceA:
    print(venceC*'C')
elif venceG>venceT and venceG>venceA and venceG>venceC:
    print(venceG*'G')

elif venceA >= venceT and venceA >= venceG and venceA >= venceC:
    if countA<countC and countA<countT and countA<countG:
        print(venceA * 'A')

elif venceT >= venceA and venceT >= venceG and venceT >= venceC:
    if countT<countC and countT<countA and countT<countG:
        print(venceT * 'T')

elif venceC >= venceT and venceC >= venceG and venceC >= venceA:
    if countC < countT and countC < countA and countC < countG:
        print(venceC * 'C')

elif venceG >= venceT and venceG >= venceA and venceG >= venceC:
    if countG < countC and countG < countA and countG < countT:
        print(venceG * 'G')