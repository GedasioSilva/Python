"""Listas em Python
    Tipo list - Mutável
    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis - índices e fatiamento
    Métodos úteis:
    append, insert, pop, del, clear, extend, +
    Create Read Update   Delete
    Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [10,20,30,40] #lista com valores
#numero = lista[2] a variavel recebe o valor dentro da lista no index 2
lista[2] = 300 #alterando o valor
print(lista[2])


del lista[3] #apagando um valor expecifico de uma string
for valores in lista:
    print(valores) #não vai aparecer o valor 40

#a função Append é pra adicionar elementos na lista
lista.append(50) #adicionar no final da lista o valor 50
print(lista[3])

#pop remove o último elemento da lista
#pode colocar um valor dentro do pop e apagar um valor especifico
ultimo_valor = lista.pop()
print(lista,'removido',ultimo_valor)

#lista.clear() é pra limpar a a lista

#insert é pra adicionar na posição escolhida
#primeiro é o lugar onde adicionar o segundo o valor a adicionar
lista.insert(0,9)
print(lista)