print("Sequência 1,2,3,...,10")
cont=1
while (cont<11):
    print(cont)
    cont = cont+1
print(" ")

print("Sequência 2,4,6...,20")
cont=2
while (cont<21):
    print(cont)
    cont = cont+2
print(" ")

print("10,9,8...1")
cont = 10
while (cont >= 1):
    print(cont)
    cont = cont-1
print(" ")

print("1,2,4,...,512")
cont=1
a=2
print("1")
while (cont < 10):
    print(a)
    cont = cont+1
    a = 2**cont
print(" ")

print("1,4,27,...(10 elementos)")
cont=1
m=1
while (m<=100):
    print(m)
    cont=cont+1
    m=cont**2
print(" ")

print("1,9,2,8,3,7,4,6,5,5")
a=1
b=9
while (a<=5) and (b>=5):
    print(a)
    print(b)
    a=a+1
    b=b-1
print(" ")

print("Múltiplos de 3 entre 10 e 40")
cont=12
while (cont<40):
    print(cont)
    cont=cont+3
print(" ")

print("Múltiplos de 51 entre 9634 e 10144")
a=9634-9634%51+51
while a<=10144:
    print(a)
    a=a+51
    