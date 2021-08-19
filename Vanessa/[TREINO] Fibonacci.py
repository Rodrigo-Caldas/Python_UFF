n = int(input())
anterior = 0
proximo = 1
soma = 0

if n == 0:
    print("0")
elif n == 1:
    print("0" + ",", "1")
else:
    for i in range(0,n):
        print(str(anterior) + ", ", end="")
        soma = proximo + anterior
        anterior = proximo
        proximo = soma
print(anterior, end="")