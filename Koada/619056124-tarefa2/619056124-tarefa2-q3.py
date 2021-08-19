N = int(input("Digite um número inteiro positivo: "))

produto = []
estoque = []
pedido = []

print("Digite",N,"produtos (separados por vírgula):")
produto = input().split(",")

e = []
print("Desses",N,"produtos, diga a quantidade deles em estoque (para separados por vírgula):")
e = input().split(",")
for i in range (0, len(e),1):
    estoque = estoque + [int(e[i])]

p = []
print("Desses",N,"produtos, diga o número de pedidos de cada um deles (para separados por vírgula):")
p = input().split(",")
for i in range (0, len(p),1):
    pedido = pedido + [int(p[i])]

dif = []
for i in range (0, len(pedido),1):
    a = pedido[i] - estoque[i]
    dif = dif + [a]

for i in range (0, len(dif),1):
    if dif[i] > 0:
        print(produto[i], dif[i])

