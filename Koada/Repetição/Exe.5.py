n = int(input("Escolha um n° inteiro para ver se é perfeito: "))
soma = 0
for i in range (1, n):
    if n % i == 0:
        soma = soma + i
if soma == n:
    print(n,"é um número perfeito.")
else:
    print(n,"não é um n° perfeito.")
