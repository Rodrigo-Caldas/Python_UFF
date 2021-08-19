import math
raio = float(input().strip())
perimetro = 2*math.pi*raio
area = math.pi*(raio**2)
print(f'{perimetro:.2f}')
print(f'{area:.2f}')