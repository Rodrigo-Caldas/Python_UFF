n = 100

def prenche_matriz():
    NM = []
    NM2 = []
    A = []
    NM = input("Digite 2 números inteiros, use espaço para separa-los: ").split(" ")
    for i in range(0, len(NM), 1):
        NM2 = NM2 + [int(NM[i])]
    print("Digite", NM2[1], "números reais, use espaço para separa-los: ")
    for i in range(0, NM2[0]):
        NM3 = input()
        numbers = list(map(float, NM3.split(" ")))
        A = A + [numbers]
    NM3 = []
    NM4 = []
    B = []
    return A

while n != 5:
    print("Opções:")
    print("(1) Preencher matriz")
    print("(2) Somar")
    print("(3) Subtrair")
    print("(4) Multiplicar")
    print("(5) Sair do programa")
    print("")
    n = int(input("Qual opção deseja? "))
    if n == 1:
        prenche_matriz()

