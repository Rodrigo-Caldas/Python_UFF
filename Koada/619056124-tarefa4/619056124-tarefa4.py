agenda=[]

#inicializando a variável "n"
n = 100

#Começando o menu de opções
while n!=0 :
    print(35 * "*", "MENU DE OPÇÕES", 35 * "*")
    print("Digite 1 para listar o nome e o telefone dos contatos da agenda")
    print("Digite 2 para listar todos os dados dos contatos que comecem com uma determinada letra")
    print("Digite 3 para inserir um novo contato e uma nova informação do contato")
    print("Digite 4 para editar um contato da agenda")
    print("Digite 5 para apagar um contato")
    print("Digite 6 para apagar todos os contatos")
    print("Digite 0 para sair do menu de opções")
    print(86*"*")
    n = int(input("Digite a opção desejada: "))
    if n == 1:
        for x in range (0,(len(agenda))):
            print(agenda[x]['Nome'],agenda[x]['telefone'])
    elif n == 2:
        letra = str(input("Digite uma letra que deseja procurar na agenda: "))
        for x in agenda:
            a = str(x['Nome'])
            if a[0] == letra:
                print(agenda[x])
    elif n == 3:
        nome, telefone = input("Digite o nome do contato, em seguida coloque uma vírgula e digite o número dele: ").split(",")
        contato = {'Nome': nome, 'telefone': telefone}
        op = input("Gostaria de adicionar um novo campo para este contato? (digite 'sim' ou 'não') ")
        if op == "sim" :
            a = input("Digite um novo campo: ")
            contato[a] = input("Digite a informação desse novo campo: ")
            agenda.append(contato)
            print("Novo contato e com um novo campo adicionado!")
        else:
            agenda.append(contato)
            print("Novo contato adicionado!")
    elif n == 4:
        print("Digite o contato que deseja modificar:")
        for x in range(0, len(agenda)):
            print("Digite", x, "para modificar o contato de", agenda[x]['Nome'])
        a = int(input())
        print("Qual informação gostaria de modificar nesse contato?")
        for key in agenda[a]:
            print("Digite a palavra '" + key + "' para mudar " + agenda[a][key])
        b = str(input())
        agenda[a][b] = input("Mudaremos o conteúdo do campo "+b+", digite o novo conteúdo desse campo: ")
        print("Mudança realizada!")
    elif n == 5:
        print("Qual contato gostaria de apagar?")
        for i in range (0,len(agenda)):
            print("Digite",i,"para excluir o contato de", agenda[i]['Nome'])
        a = int(input())
        agenda.pop(a)
        print("Contato apagado!")
    elif n == 6:
        for x in range (0,(len(agenda))):
            agenda.pop(0)
        print("Contatos apagados!")
print("Obrigado por utilizar o sistema! Até logo")

