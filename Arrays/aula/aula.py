#uma array é uma lista que pode receber diversos itens
#devo utilizar uma Array quando uma lista ficar muito grande
#só vale a pena criar array se for muitos itens acima de mil
from array import array

letras = ['a','b','c','d']
numeros_i = [10,20,30,40]
numeros_f = [1.2,2.2,3.2]

print(letras)
print(numeros_i)
print(numeros_f)

print(" ")

letras = array('u',['a','b','c','d']) #lista de string usa o " u"
array_inteiros = array('i',[10,20,30,40]) #array de inteiro usa i
array_floats = array('f',[1.2,2.2,3.2]) #array de float usa o f

print(letras)
print(array_inteiros)
print(array_floats)
