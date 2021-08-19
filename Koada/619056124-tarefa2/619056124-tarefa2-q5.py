C = []
D = []
n = int(input("Digite o grau do polinômio: "))
D = input("Digite os valores dos coeficientes (do maior ao menor grau) e o valor da variável separados por espaço: ").split(" ")

for i in range (0, len(D),1):     #Esse loop vai transformar todos os elementos em string na lista D em números reais. E vai salva-los em uma nova lista.
    C = C + [float(D[i])]

valor = 0                         #Declaro essa variável pois usarei ela para armazenar a soma de todos os valores da equação

for i in range (0, len(C)-1,1):   #Esse loop vai calcular todos os termos da equação e armazena-los na variável "valor".
    v = C[i]*(C[len(C)-1]**n)
    valor = valor + v
    n = n-1

print(valor)
