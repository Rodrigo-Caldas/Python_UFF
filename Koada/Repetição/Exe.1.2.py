num = int(input("Digite um número inteiro positivo qualquer: "))
contador = 0
while num >= 1:
    num = num/10
    contador = contador + 1
print("O seu número tem", contador ,"dígito(s)." )


