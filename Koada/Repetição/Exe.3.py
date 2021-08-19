n = int(input("Escolha um número inteiro qualquer: "))
cont = 0
for i in range(1,n+1):
    if n % i == 0:
        print(i)
        cont = cont + 1
if cont > 2:
    print("Não é um n° primo.")
elif cont <= 2:
    print("É um n° primo.")
a = input("Deseja testar um novo número? (sim ou não): ")
while a == "sim":
    n = int(input("Escolha um número inteiro qualquer: "))
    cont = 0
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
            cont = cont + 1
    if cont > 2:
        print("Não é um n° primo.")
    elif cont <= 2:
        print("É um n° primo.")
    a = input("Deseja testar um novo número? (sim ou não): ")
print("Até a próxima!")
