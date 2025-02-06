print(" ")

#Lista e Generator Expressions 

from sys import getsizeof

#Generator Expressions 
    #uma forma mais rápida para Listas , dicionarios e etc
    #menos memoria alocada valores em byte

#mostrar a forma que podemos economizar os bytes
numeros = [x * 10 for x in range(100)]
print(type(numeros))
print(getsizeof(numeros))

print(" ")

numeros = (x * 10 for x in range(100))
print(type(numeros))
print(getsizeof(numeros))   