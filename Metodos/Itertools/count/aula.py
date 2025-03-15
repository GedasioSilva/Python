#Count é um iterador sem fim (itertools)
#toda a vez que colocar next c1 vai adicionar um número
#count é um contador onde não sabemos o fim

from itertools import count #importando o count no modulo itertools

c1 = count(0)
r1 = range(10)

# o intervael tem o metodo iter e nex
print('c1',hasattr(c1, '__iter__')) #verifica se é um interavel
print('c1',hasattr(c1, '__next__')) # verificando se ele tem o metodo next

print('Count')
for i in c1: #toda vez que o c1 é verificado ele adiciona mais 1 até  o valor 10
    if i > 10:
        break
    print(i)

print(" ")
#aqui não precisa travar pq o r1 tem um fim que é o valor 10
for i in r1: #toda vez que o c1 é verificado ele adiciona mais 1 até  o valor 10
    print(i)    