# BOAS VINDAS
print("Seja bem vindo senhor usuário, o objetivo desse programa é ordenar um vetor.")
# DIÁLOGO DE ENTRADA DE DADOS
arq_dados = open("INTEIROS 20", "r")  # associando INTEIROS 20 ao arq_dados
a = list(map(int, arq_dados.readline().split(" ")))
print("O vetor lido foi: \n", a)
# PROCESSAMENTO
l = len(a) - 1
troca = 1  # apenas para garantir a primeira execução do while
trocas = 0
ifs = 0
while troca != 0:
    troca = 0
    for i in range(0, l, 1):
        ifs = ifs + 1
        if a[i] > a[i + 1]:  # se estão fora da ordem...
            aux = a[i]
            a[i] = a[i + 1]  # Põe no lugar
            a[i + 1] = aux
            troca = troca + 1
    l = l - 1  # mais um elemento no lugar
    trocas = trocas + troca
    print(a, "Troca:", troca)
# EMISSÃO DE RELATÓRIO DE SAÍDA
print("Após a ordenação, o vetor ficou:\n", a)
print("Foram realizadas:", trocas, "trocas e", ifs, "ifs")
# DESPEDIDA
print("Fim do programa. Obrigado por utilizar")
# FINALIZAÇÃO
#   <comandos para o encerramento do programa, se houver>
