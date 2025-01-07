#a função Len() é utilizada pra fazer a contagem de elementos

#usando a len pra contar os caracteres da variavel nome
nome = "gedasio"
print(len(nome))

#contar elementos de uma lista
lista = [1,2,3,4,5]
print(len(lista))

#count é um metodo 
#utilizando pra contar quantas vezes o número 2 aparece
lista2 = [3,3,5,7,8,9,3]
print(lista2.count(3)) # o numero apareceu 3 vezes 

#contar items unicos 
listaFrutas = ['manga','uva','goiaba','uva','manga']
itens_unicos = set(lista)
print(len(itens_unicos))

lista3 = [1,2,3,4,5,6]

pares = [x for x in lista3 if x % 2 == 0]
print(len(pares))

