import math      #Importando a biblioteca
## Primeiro Ponto
a = float(input("Digite o valor do primeiro ponto no eixo x: "))
b = float(input("Digite o valor do primeiro ponto no eixo y: "))
print("Seu primeiro ponto é:","(", a ,",", b, ")")
## Segundo Ponto
c = float(input("Digite o valor do segundo ponto no eixo x: "))
d = float(input("Digite o valor do segundo ponto no eixo y: "))
print("Seu segundo ponto é:","(", c ,",", d, ")")
## Diferença entre os dois pontos
dx = a - c
dy = b - d
## Função que vai calcular a distãncia entre esses pontos
e = math.sqrt(dx*dx + dy*dy)
print(e)