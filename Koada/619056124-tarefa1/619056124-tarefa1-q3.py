import math
x = int(input("Insira um número inteiro: "))
a = int(math.sqrt(x))
if a**2 == x:
    print(a,"é raiz quadrada de",x)
else:
    print(x,"não possui raiz quadrada inteira.")