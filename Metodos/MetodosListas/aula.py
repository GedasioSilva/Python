#append(): Adiciona  "um" elemento ao final da lista.
lista = [2,1]
lista.append(3)
print(lista)

#extend(): Adiciona múltiplos elementos de outra lista ou iterável.
lista.extend([5,6])
print(lista)

#insert(): Insere um elemento em uma posição específica.
lista.insert(6, 7)  # lista: [1, 2, 3]
print(lista)

#remove(): Remove a primeira ocorrência de um valor.
#remove a primeira vez que o 5 for encontrado
lista.remove(5)
print(lista)

#pop(): Remove e retorna o elemento de uma posição (ou o último por padrão). no caso remove o 7
lista.pop()
print(lista)

#sort(): Ordena a lista (inplace).
lista.sort()
print(lista)