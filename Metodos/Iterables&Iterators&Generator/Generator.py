#Generator Expression 
#Generator é uma função que mostra um valor por vez
#e não guarda tudo na memoria de um unica vez
import sys

generator = (n for n in range(3))

print(sys.getsizeof(generator)) #pega o tamano em bits
print(generator) #é um generetion ai mostra um valor por vez
print(next(generator))
print(next(generator))

