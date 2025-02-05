#map function
    #muito utilizada com listas
    #aplica uma função a um Iterable , por item. (list,tuple,dicionario)


lista1 = [1,2,3,4] #onde ta os dados que vai ser passado pra função

def multi(x): #a função que tem a clausula matematica
    return x * 2

#map pega a função e passo os dados da lista1 pra dentro da variavel da func
lista2 = map(multi,lista1) 
print(list(lista2))


#utilizar o map com a função lambda
lista3 = [1,2,3,4]


#pega a lista3 e passa os dados pra dentro da lambda
#peguei a lista joguei pra dentro de lambda e em lambda multipliquei por 2 
print(list(map(lambda x: x * 2 , lista3)))
#print list pra mostrar como uma lista
#o map pra poder juntar uma lista com uma função