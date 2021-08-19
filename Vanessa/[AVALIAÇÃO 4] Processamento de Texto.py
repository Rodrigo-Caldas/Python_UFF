texto1 = input().strip()

# Transformando as palavras em listas
lista1 = input().strip().split(" ")  #Voce vai usar essa variavel para o print das palavras no final

# Colocando as palavras em maiúsculo
lista_texto = " ".join(lista1)
lista2 = lista_texto.upper()
lista3 = list(lista2.split()) #Vai usar essa pra comparar

# Transformar o texto em lista e tirar as vírgulas e pontos
texto_lista = []

for i in range(0, len(texto1)):
    if texto1[i] != ',' and texto1[i] != ';' and texto1[i] != '.' and texto1[i] != '!' and texto1[i] != '?':
        texto_lista = texto_lista + list(texto1[i])

# Aqui transformamos a lista em string novamente e colocamos todas em maiúsculo
texto2 = "".join(texto_lista)
texto3 = texto2.upper()

# Aqui colocamos todas as palavras em maiúsculo em lista
texto_lista2 = list(texto3.split(" "))  #vai usar essa lista para comparação das palavras

#Contar quantas vezes as palavras aparecem no texto
lista_cont = []
cont = 0
for r in range(0,len(lista3)):
    cont = 0
    for i in range(0,len(texto_lista2)):
        if lista3[r] == texto_lista2[i]:
            cont = cont + 1
    lista_cont = lista_cont + [int(cont)]

print(len(texto_lista2))
for i in range(0, len(lista1)):
    print(lista1[i],lista_cont[i])

maximo = max(lista_cont)
posicao = 0

for i in range(0, len(lista1)):
    if maximo == lista_cont[i]:
        posicao = i

percentual = (maximo*100)/len(texto_lista2)
percentual = round(percentual,2)

if percentual != 0:
    print(lista1[posicao], str(percentual)+"%")