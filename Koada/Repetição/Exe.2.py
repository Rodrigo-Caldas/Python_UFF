print("~"*30)
print("Sequência de Fibonacci")
print("~"*30)
n = int(input("Escolha um número inteiro positivo qualquer: "))
n1 = 0
n2 = 1
cont = 3
print(n1 , "," , n2 , end="")
while n+1 != cont:
    n3 = n1 + n2
    print(" ," , n3 , end="")
    n1 = n2
    n2 = n3
    n = n - 1
print(" , fim da sequência.")
