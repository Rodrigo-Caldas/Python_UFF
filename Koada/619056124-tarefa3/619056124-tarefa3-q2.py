NM = []
NM2 = []
A = []

NM = input("Digite 2 números inteiros, use espaço para separa-los: ").split(" ")
for i in range (0, len(NM),1):
    NM2 = NM2 + [int(NM[i])]

#Criando a matriz que o usuário digitou com N linhas e M colunas
print("Digite", NM2[1],"números reais, use espaço para separa-los: ")
for i in range (0 , NM2[0]):
    NM3 = input()
    numbers = list(map(float, NM3.split(" ")))
    A = A + [numbers]

#Criando uma matriz nula com M linhas e N colunas
B = []
for i in range(NM2[1]):
    linha = [0]*NM2[0]
    B.append(linha)

#Trocando os elementos da Matriz B pelos elementos da Matriz A
for i in range (NM2[0]):
    for c in range (NM2[1]):
        B[c][i]=A[i][c]

#Mostrando a Matriz transpota B, com duas casas decimais
for i in range (0,len(B)):
    for c in range (0, len(B[i])):
        print(f"{B[i][c]:5.2f}", end=" ")
    print()

#Multiplicação de B x A

BA = []
for i in range(0, len(B), 1):
    L = []
    for j in range(0, len(A[0])):
        s = 0  # ACUMULA OS PRODUTOS
        for k in range(0, len(B[0])):
            s = s + B[i][k] * A[k][j]
        L.append(s)
    BA.append(L)

#Mostrando a Matriz BA, com duas casas decimais
for i in range (0,len(BA)):
    for c in range (0, len(BA[i])):
        print(f"{BA[i][c]:5.2f}", end=" ")
    print()

