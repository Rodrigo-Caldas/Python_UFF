distancia = int(input().strip())
combustivel = int(input().strip())

for d in range (1,distancia+1):
    soma_impar=0
    for i in range (1,d,2):
        soma_impar = soma_impar + i
        #print("valor de", d , i , soma_impar)
    consumo = distancia/(soma_impar + 1)
    combustivel = combustivel - consumo
    if combustivel < 0:
        break
    print(d,int(combustivel))
