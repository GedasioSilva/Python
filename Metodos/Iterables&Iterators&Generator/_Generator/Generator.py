#Generator Expression 
#Generator é uma função que mostra um valor por vez
#e não guarda tudo na memoria de um unica vez
#o genereitor vai atualizando o valor quando passo next
import sys

lista = [n for n in range(10000)] 
generator = (n for n in range(10000))

#o generator é pequeno quando usamos uma lista muito grande
#devemos utilizar o generator pra deixar o programa mais leve

print(sys.getsizeof(generator)) #pega o tamano em bits
print(sys.getsizeof(lista))#pegando o tamanho em bits
#print(generator) é um generetion ai mostra um valor por vez
print(next(generator))
print(next(generator))

