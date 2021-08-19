L = []
n = 1
while n != 0:
    n = float(input("Insira um número real positivo, digite 0 para parar: "))
    if n != 0:
        L = L + [n]

print(L, len(L))

i = 0
t = len(L)
G = []

while i < t or i == t:
    g = (L[i] + L[t-1]) / 2
    G = G + [g]
    t = t-1
    i = i+1


if len(L) % 2 == 0:
    G.pop()

for i in range (0,len(G),1):
    print(G[i])