print("Bem vindo sr.usuario")
arqdados = open("INTEIROS 20", "r")  # associando arquivo externo(inteiros 20.txt ao arqdados)
a=list(map(int,arqdados.readline().split(" ")))
print("vetor lido: \n" , a)
ifs=0                              #contará ifs
trocas = 0  # contará trocas
for f in range (0,len(a)-1,1):
    MEN = f  # HIPOTESE INICIAL
    for i in range(f + 1, len(a), 1):  # percorrer todos os outros
        if a[i] < a[MEN]:
            MEN = i  # novo campeão
        ifs = ifs + 1
    aux = a[f]
    a[f] = a[MEN]
    a[MEN] = aux
    trocas = trocas + 1
print("Após a ordenação ficou: \n",a)
print("foram executados", ifs," ifs e", trocas,"trocas")