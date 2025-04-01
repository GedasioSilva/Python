#Generator expression , Iterables e Iterators em Python 
#intereitor precisa deter os valores 
#itrare é como se os numeros tivem em ordem e quando passamos o next
#chama outro número que tava na ordem até acabar os valores só isso

iterable = ['eu','tenho','__iter__']
#a unica responsabilidade ele só sabe o proximo valor
iterator = iterable.__iter__()
# no caso ele só sabe o proximo valor a função next vai atualizando os valor
print(next(iterator)) 
print(next(iterator)) 
print(next(iterator)) 

print(20*"--")

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