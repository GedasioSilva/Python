#Generator expression , Iterables e Iterators em Python 
#precisa deter os valores 
iterable = ['eu','tenho','__iter__']

#a unica responsabilidade ele só sabe o proximo valor
iterator = iterable.__iter__()
print(next(iterator)) # no caso ele só sabe o proximo valor a função next vai atualizando os valor

print(" ")

#iterables tem que ter o __iter__
# o iterator tem que receber rum iterables

itera = ['Gedasio','Camila','Diana','__iter__']
iterator2 = iter(itera)
print(iterator2) 
#iterator vai atualizando os valores como se fosse um Array

for indece in itera:
    print(next(iterator2))
    #quando ele chegar no Último ele retorna o valor __iter__
#usei o index pra fazer o next ate o iterator2 acabar 