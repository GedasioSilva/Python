#filter function 
    #muito utilizada com listas 
    #aplica uma função a um Iterable , por item. (list,tuple,dicionario)
    #o map eu consigo adicionar uma lista em uma função com o filter faço o mesmo só que retirando o valor do retorno
    
valores = [10,12,34,44,57]

def remover20(x):
    return x > 20    

#passando os valores da lista pra dentro da função Remover20
print(list(filter(remover20,valores)))
print(list(filter(lambda x: x > 20,valores)))
#retornar o valores que forem maior que 20