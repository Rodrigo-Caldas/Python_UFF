n = 0
vinhos = []
while n != -1:
    n = int(input().strip())
    if n == 1:
        linha = []
        for i in range(0,3):
            a = input().strip()
            if i == 2:
                a = int(a)
            linha.append(a)
        vinhos.append(linha)
    elif n == 2:
        nome = input().strip()
        soma = 0
        tipo = 0
        for i in range(0,len(vinhos)):
            if nome == vinhos[i][0]:
                soma = soma + vinhos[i][2]
                tipo = vinhos[i][1]
        if soma == 0:
            print("Não cadastrado")
        else:
            print(tipo)
            print(soma)
    elif n == 3:
        tipo = input().strip()
        soma = 0
        for i in range(0,len(vinhos)):
            if tipo == vinhos[i][1]:
                soma = soma + vinhos[i][2]
        if soma == 0:
            print("Não cadastrado")
        else:
            print(soma)
    elif n == 4:
        soma = 0
        for i in range(0,len(vinhos)):
            soma = soma + vinhos[i][2]
        print(soma)
    elif n > 4 or n < -1:
        print("Inválido")