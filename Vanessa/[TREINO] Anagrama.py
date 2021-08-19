palavra1 = input().strip()
palavra2 = input().strip()

palavra11 = palavra1.upper()
palavra22 = palavra2.upper()

a = 0
if len(palavra1) == len(palavra2):
    for i in range(0, len(palavra1)):
        for x in range(0, len(palavra2)):
            if palavra11[i] == palavra22[x]:
                a = a + 1
    if a == len(palavra1):
        print("True")
    else:
        print("False")
else:
    print("False")
