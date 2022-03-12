import random
a = [random.randint(0,99) for i in range(0,20,1)]
print("vetor gerado: ", a)
MEN=0        # hipótese inicial
for i in range(1,len(a),1):    #percorrer todos os outros
    if a[i] < a[MEN]:
        MEN= i
print("O elemento de menor valor está na posição ",MEN, "e seu valor é de", a[MEN])