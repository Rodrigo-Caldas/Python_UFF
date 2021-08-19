num_doc = input()                        #numero do documento
regras_cumpridas = 0                     #contador de regras cumpridas

if len(num_doc) == 6:
    print("True")
    regras_cumpridas = regras_cumpridas + 1
else:
    print("False")

if len(num_doc) < 4 or len(num_doc) < 2:
    print("False")
elif ((int(num_doc[1])**4)%3) == 0 and ((int(num_doc[3])**4)%3) == 0:
    print("True")
    regras_cumpridas = regras_cumpridas + 1
else:
    print("False")

if len(num_doc) < 3 or len(num_doc) < 2:
    print("False")
elif num_doc[2] != 0 or num_doc[2] != 1:
    print("True")
    regras_cumpridas = regras_cumpridas + 1
else:
    print("False")

if len(num_doc) < 6:
    print("False")
elif int(num_doc[2])+int(num_doc[5]) > 3:
    print("True")
    regras_cumpridas = regras_cumpridas + 1
else:
    print("False")

if len(num_doc) < 1:
    print("False")
elif int(num_doc[0]) == 2 or int(num_doc[0]) == 5 or int(num_doc[0]) == 9:
    print("True")
    regras_cumpridas = regras_cumpridas + 1
else:
    print("False")

if regras_cumpridas == 5:
    print("True")
else:
    print("False")