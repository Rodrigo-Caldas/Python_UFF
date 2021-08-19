a = int(input("Vamos verificar se um número de 6 dígitos é palíndromo, escolha o primeiro dígito: "))
b = int(input("Agora o segundo dígito: "))
c = int(input("O terceiro: "))
d = int(input("O quarto: "))
e = int(input("O quinto: "))
f = int(input("O sexto: "))

if a == f and b == e and c == d:
    print("O número",a,b,c,d,e,f,"é palíndromo")
else:
    print("O número",a,b,c,d,e,f,"não é palíndromo")