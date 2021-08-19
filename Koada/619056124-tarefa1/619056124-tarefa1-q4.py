import math      #Importando a biblioteca
## Primeiro Ponto
a = float(input("Digite o valor do primeiro ponto no eixo x: "))
b = float(input("Digite o valor do primeiro ponto no eixo y: "))
print("Seu primeiro ponto é:","(", a ,",", b, ")")
## Segundo Ponto
c = float(input("Digite o valor do segundo ponto no eixo x: "))
d = float(input("Digite o valor do segundo ponto no eixo y: "))
print("Seu segundo ponto é:","(", c ,",", d, ")")
## Terceiro Ponto
e = float(input("Digite o valor do terceiro ponto no eixo x: "))
f = float(input("Digite o valor do terceiro ponto no eixo y: "))
print("Seu terceiro ponto é:","(", e ,",", f, ")")
## Diferença entre os três pontos
dx = a - c
dy = b - d

dx2 = a - e
dy2 = b - f

dx3 = c - e
dy3 = d - f
## Função que vai calcular a distãncia entre esses pontos
g = math.sqrt(dx*dx + dy*dy)
h = math.sqrt(dx2*dx2 + dy2*dy2)
i = math.sqrt(dx3*dx3 + dy3*dy3)

if g + h > i and h + i > g and i + g > h:
    print("Os pontos dos vértices que escolheu formam um triângulo.")
    if g == h and g == i:
        print("O triângulo é equilátero")
    elif g == h and g != i:
        print("O triângulo é isósceles")
    elif h == i and h != g:
        print("O triângulo é isósceles")
    elif g == i and g != h:
        print("O triângulo é isósceles")
    elif h != i and h != g:
        print("O triângulo é escaleno")
else:
    print("Os pontos dos vértices que escolheu não podem formar um triângulo.")