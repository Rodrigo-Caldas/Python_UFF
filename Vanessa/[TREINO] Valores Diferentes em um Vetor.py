vetor =[]
for i in range (0,10):
    numero = int(input().strip())
    vetor.append(numero)
a = 1
for x in range(0,len(vetor)):
    if vetor[x] != vetor[0]:
        a = a + 1
print(a)

