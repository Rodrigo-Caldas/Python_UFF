x = int(input())
y = 0
soma = 0

while len(str(soma)) <= 5:
    soma = 0
    for z in range(0, y+1):
        fatorial = 1
        for g in range(1, (2*z)+1):
            fatorial *= g
        soma += (((-1) * z) / (fatorial)) * ((x) * (2 * z))
    y += 1

print(soma)
