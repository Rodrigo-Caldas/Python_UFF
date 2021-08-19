import random as r
a = r.randint(1,100)
b = r.randint(1,100)
c = r.randint(1,100)
d = r.randint(1,100)
e = r.randint(1,100)
x = 0 #Contador de número par
y = 0 #Contador de número ímpar

if (a%2) == 0:
    print(a,"é um númeor par.")
    x = x + 1
else:
    print(a,"é um número ímpar.")
    y = y + 1

if (b%2) == 0:
    print(b,"é um númeor par.")
    x = x + 1
else:
    print(b,"é um número ímpar.")
    y = y + 1

if (c%2) == 0:
    print(c,"é um númeor par.")
    x = x + 1
else:
    print(c,"é um número ímpar.")
    y = y + 1

if (d%2) == 0:
    print(d,"é um númeor par.")
    x = x + 1
else:
    print(d,"é um número ímpar.")
    y = y + 1

if (e%2) == 0:
    print(e,"é um númeor par.")
    x = x + 1
else:
    print(e,"é um número ímpar.")
    y = y + 1

print("Temos",x,"números pares e",y,"números ímpares.")
