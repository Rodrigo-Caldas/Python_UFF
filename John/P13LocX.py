print("Localizando um valor em um vetor por busca sequencial")
A = [5, 4, 9, 7, 6, 2, 3, 11, 15, 20]
print("O vetor original é:", A)
x = int(input("Digite um número para x: "))
print("O número escolhido foi: ", x)
A.append (x)         #adiciono a varável x no final da lista
print(A)
i = 0
while(A[i]!=x):
    i = i + 1
if i > len(A)-2:
    print(x, "não está no vetor")
else:
    print(x, "aparece na posição", i)
A.pop ()             #Apaga a variável x no final da lista
print("vetor A restaurado:",A)

def impvetor (vet,frase):
    print(frase,vet)

impvetor([2,3,4,8,9,6], "Vetor lido:")