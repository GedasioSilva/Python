numeros = [1,2,3,4,5,6]

#vai retorna os quadrados dos numeros da lista
quadrado = lambda x : x ** 2
resultado = []

#pegar a lista resultado e adiciona a função que recebe o numero
# esse numero vai ser o x da lambda onde o x é multiplicado por ele mesmo

for numero in numeros:
    resultado.append(quadrado(numero))

print(resultado)

print("")
#Utilizando lamda pra ordenar uma lista

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
#a função recebe a lista
#for item in lista e depois motra o item a ordem vem da lambda
def exibir(lista):
    for item in lista:
        print(item)
    print()    

#variavel l1 usa o metodo sorted ordernar a lista
#key é uma função que recebe a lambda a lambeda tem uma variavel
#item recebe o index nome
l1 = sorted(lista, key=lambda item:item['nome'])

#mostrando a l1
exibir(l1)
