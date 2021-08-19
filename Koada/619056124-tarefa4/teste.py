# criando um catálogo de livro
catalogo = []
# criando um livro usando dicionário
livro={"título":"Grande Sertão Veredas","autor":"João Guimarães Rosa"}
catalogo.append(livro)
# criando um outro livro
livro={"título":"Os irmãos Karamazov","autor":"Fiódor Dostoiévski"}
catalogo.append(livro)
# mostrando o catálogo
print("------- Mostrando o catálogo ------------")
for livro in catalogo:
    print (livro)
# criando um outro livro
livro={"título":"O jogador","autor":"Fiódor Dostoiévski","edição":1}
catalogo.append(livro)
# mostrando o catálogo
print("------- Mostrando o catálogo ------------")
for livro in catalogo:
    print (livro)
# incluíndo uma nova chave no 1o registro
catalogo[0]['edição']=1
print("------- Mostrando o catálogo [com nova chave] ------------")
for livro in catalogo:
    print (livro)
# mostrando os livros cuja edição é igual a 1
print("------- Mostrando os livros cuja edição é igual a 1 ------------")
for livro in catalogo:
    if "edição" in livro.keys() and livro["edição"]==1:
            print(livro)
# incluir "língua original"="russo" para os livros do Fiódor Dostoiévski"
for i in range(len(catalogo)):
    if catalogo[i]["autor"]=="Fiódor Dostoiévski":
        catalogo[i]["língua original"]="russo"
print("------- Mostrando o catálogo [com nova chave] ------------")
for livro in catalogo:
    print (livro)