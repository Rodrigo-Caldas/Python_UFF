n = int(input("Escolha um n° inteiro: "))
i = 1
while i * (i+1) * (i+2) < n:
    i = i + 1
if i * (i+1) * (i+2) == n:
    print("%d é um n° triangular e produto de %d*%d*%d." % (n, i, i + 1, i + 2))
else:
    print("%d não é triangular." % (n))

