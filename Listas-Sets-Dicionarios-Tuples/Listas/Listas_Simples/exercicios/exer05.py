#crie duas lista de valores e crie outra lista com os valores de
#cada index das duas listas somados

l1 = [1,2,3,4,5]
l2 = [2,3,5,4,6,7,9]
lista_soma = []

#for i in range(len(l1)): #verifica até onde o i vai rodar
#    lista_soma.append(l1[i] + l2[i]) #lista_soma recebe l1 + l2
#print(lista_soma)

print(10*"-","Outra Forma de fazer",10*"-")
#lista comprehension
#criando a variavel x e y for x , y in zipe na junção das duas listas
lista_soma = [x + y for x , y in zip(l1,l2)]
print(lista_soma)